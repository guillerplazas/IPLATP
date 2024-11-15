import asyncio
from isabelle_client import get_isabelle_client, start_isabelle_server, IsabelleResponse
import openai
import nest_asyncio
import pandas as pd
import json
import logging
import os
from IPython.display import display, HTML
from typing import List

nest_asyncio.apply()
MAX_ATT = 8
openai.api_key = "" 
SYS = " ".join(["Please for the given Isabelle/HOL lemma,",
        "provide a the necessary steps to complete the formal proof.",
        "Provide always Isabel code, and use comments and the sorry", 
        "command to indicate the steps that need to be completed.",])

def interpret_proof_result(response, responses: List[IsabelleResponse]):
    errors = []
    response_lines = response.split('\n')
    
    # Find sorry statement if there exists one
    for i, line in enumerate(response_lines):
        if "sorry" in line or "Sorry" in line:
          errors.append(f"line {i+1} Sorry statement found, correct it.")
    
    for response in responses:
        # Only explore certain type of messages of the isabelle_client
        if response.response_type in ["FINISHED", "ERROR", "FAILED"]:
            body = json.loads(response.response_body)
            for error in body.get('errors', []):
                message = error.get('message', '')
                pos = error.get('pos', {})
                if "\\<^here>" in message:
                  parts = message.split("\\<^here>")
                  printer=f"line {pos.get('line','unknown')-5} {parts[0]}"
                  for part in parts[1:]:
                        printer += part
                  printer = printer.replace('\n', ' ')
                  errors.append(printer)
    return errors

def create_theory_content(result,idx):
        return f"""theory aux_{idx}
    imports Complex_Main

begin

{result}

end
    """

def create_error_prompt(solution, errors):
        error_message = "\n".join(errors)
        return f"""Please correct the following proof:
isabelle
{solution}

It returns the following errors: 
{error_message}
   """

def insert_errors_as_comments(proof: str, errors: List[str]) -> str:
    lines = proof.split('\n')
    for error in errors:
        if error.startswith("line"):
            try:
                # Extracting the line number from the error message
                line_num = int(error.split(" ")[1])
                error_message = error.split(" ", 2)[2].strip()
            except (IndexError, ValueError):
                continue  # Skip issues while parsing
            # Writting error in line
            if 0 <= line_num - 1 < len(lines):
                lines[line_num-1] += f"  (* ERROR: {error_message} *)"
    return f"""Correct the proof. The errors are annotated as comments:
isabelle
{"\n".join(lines)}

   """
    

async def complete_solution(ex: str, prob_num: int, attempt: int):
    cont=[{"role": "system", "content": SYS}, 
          {"role": "user", "content": ex}]
    res_pre = await asyncio.get_event_loop().run_in_executor(None, lambda: 
        openai.chat.completions.create(model="gpt-4o", messages=cont, n=1,))
    res = res_pre.choices[0].message.content.split('```isabelle')[1].split('```')[0]
    res_disp=res_pre.choices[0].message.content.replace("\n", "<br>")

    # Code to display the response in a scrolling table
    df = pd.DataFrame([res_disp],columns=[f"Problem. {prob_num}- Attempt. {attempt+1}"])
    css =""" 
    <style>
        .dataframe td {
            white-space: nowrap;
            text-align: left; 
        }
        .scrolling-wrapper {
            overflow-x: auto;
        }
    </style>
    """
    html = f"{css}<div class='scrolling-wrapper'>{df.to_html(escape=False, index=False)}</div>"
    display(HTML(html))
    return res

async def process_problem(theory, n_prob, client, succ_count,max_att=MAX_ATT):
    current_prompt = theory
    for att in range(max_att):
        # Get the solution from the LLM
        solution = await complete_solution(current_prompt, n_prob, att)
        theory_content = create_theory_content(solution, n_prob)
        
        # Write theory file for Isabelle client
        file_path = os.path.join('./auxs', f"aux_{n_prob}.thy")
        with open(file_path, 'w') as file:
            file.write(theory_content)
        
        # Use theory with Isabelle client
        response = await asyncio.get_event_loop().run_in_executor(None, lambda: 
            client.use_theories([f"aux_{n_prob}"], master_dir='./auxs'))
        errors = interpret_proof_result(solution, response)
        
        if not errors:
            print(f"PROBLEM {n_prob} SOLVED AFTER {att+1} ATTEMPTS\n{'_'*40}\n")
            succ_count[0] += 1
            return True
        else:
            # Select one of the prompt options: 
            current_prompt = theory 
            #current_prompt = create_error_prompt(solution, errors)
            #current_prompt = insert_errors_as_comments(solution, errors)
    
    print(f"PROOF NOT FOUND FOR PROBLEM {n_prob} AFTER {max_att} ATTEMPTS\n{'_'*40}\n")
    return False

async def worker(client, theory_queue, success_counter):
    while True:
        if theory_queue.empty():
            break
        num_prob, theory = await theory_queue.get()
        await process_problem(theory, num_prob, client, success_counter)
        theory_queue.task_done()

async def benchmark(theory_files):
    server_info, _ = start_isabelle_server()
    clients = [get_isabelle_client(server_info) for _ in range(4)]
    theory_queue = asyncio.Queue()
    success_count = [0]

    for index, theory in enumerate(theory_files, start=1):
        await theory_queue.put((index, theory))

    # Create worker tasks for each client
    for client in clients:
        tasks = [asyncio.create_task(worker(client, theory_queue, success_count))]
    
    await theory_queue.join()  # Wait until all tasks are done
    await asyncio.gather(*tasks)  # Ensure all worker tasks are finished

    print(f"\nSCORE: {success_count[0]} out of {len(theory_files)}")




