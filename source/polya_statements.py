polya_statements = [
    'lemma "(0::real) < u ==> u < v ==> v < 1 ==> 2 <= x ==> x <= y ==> 2 * u * v^2 < v * y^2"', #1
    'lemma "(0 :: real) < 1 + y^2"', #2
    'lemma "(1::real) < x ==> (1 + y^2) * x > (1 + y^2)"', #3
    'lemma "(0::real) < x ==> x < 1 ==> 1 / (1 - x) > 1 / (1 - x^2)"', #4
    'lemma "(0::real) < u ==> u < v ==> 0 < z ==> z + 1 < w ==> (u + v + w)^3 < (u + v + w + 1)^5"', #5
    'lemma "(0::real) < u ==> u < v ==> 0 < z ==> z + 1 < w ==> (u + v + w)^33 < (u + v + w + 1)^55"', #6
    'lemma "(0::real) < u ==> u < (v^2 + 23)^3 ==> 0 < z ==> z + 1 < w ==> (u + (v^2 + 23)^3 + w)^3 < (u + (v^2 + 23)^3 + w + 1)^5"', #7
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> (x::real) <= y ==> u + f x < v + f y"',  #8
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> 1 < v ==> (x::real) <= y ==> f x + u < v^2 + f y"', #9
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> 1 < w ==> 2 < s ==> (w + s) / 3 < v ==> (x::real) <= y ==> f x + u < v^2 + f y"', #10
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> 1 < v ==> (x::real) <= y ==> f x + u < (1 + v)^10 + f y"', #11
    'lemma "(ALL x. f x <= 1) ==> (0::real) < w ==> u < v ==> u + w * f x < v + w"' #12
    'lemma "(ALL x. f x <= 2) ==> (0::real) < w ==> u < v ==> u + w * (f x - 1) < v + w"', #13
    'lemma "(z :: real) > exp x \<Longrightarrow> w > exp y \<Longrightarrow> z^3 * w^2 > exp (3 * x + 2 * y)"', #14
    'lemma "(u::real) > 0 \<Longrightarrow> v > 0 \<Longrightarrow> x > 0 \<Longrightarrow> ln x > 2 * u + v \<Longrightarrow> x > 1"', #15
    'lemma "(x :: real) < y \<Longrightarrow> u \<le> v \<Longrightarrow> u + min (x + 2 * u) (y + 2 * v) \<le> x + 3 * v"', #16
    'lemma "y > (0::real) \<Longrightarrow> abs (3 * x + 2 * y + 5) < 4 * abs(x) + 3 * y + 6"', #17
    'lemma "(u::real) > 0 \<Longrightarrow> v > 0 \<Longrightarrow> root 3 (u^9 * v^4) > u^3 * v"', #18
    'lemma "exp(max (abs (x::real)) y) \<ge> 1"', #19
    'lemma "y > (0::real) \<Longrightarrow> ln (1 + abs(x) + y) > 0"', #20
    'lemma "y > 0 \<Longrightarrow> ln (1 + abs(x) + y^4) > 0"',    #21
    'lemma "(0::real) < x ==> x < y ==> u < v ==> 2 * u + exp (1 + x + x^4) <= 2 * v + exp (1 + y + y^4)"', #22
    'lemma "(0::real) < x ==> 3 < y ==> (u::real) < v ==>2 * u + exp 10 <= 2 * v + exp (1 + y^2)"', #23
    'lemma "(ALL (x::real) y. f(x + y) = f(x) + f(y)) ==> f(a + b) > (2::real) ==> f(c + d) > 2 ==>f(a + b + c + d) > 4"', #24
    'lemma "(ALL (x::real) y. f (x + y) = f x * f y) ==> f a > (2::real) ==> f b > 2 ==>f(a + b) > 4"', #25
    'lemma "(0::real) <= n ==> n < (K / 2) * x ==> 0 < C ==> 0 < eps ==> eps < 1 ==> (1 + eps / (3 * (C + 3))) * n < K * x"',   #26
    'lemma "(0::real) < x ==> x < y ==> (1 + x^2) / (2 + y)^17 < (1 + y^2) / (2 + x)^10"', #27
    'lemma "(0::real) < x ==> x < y ==> (1 + x^2) / (2 + exp y) < (1 + y^2) / (2 + exp x)"', #28
    'lemma "(0::real) < x ==> 0 < y ==> y < 1 ==> x + y > x * y"', #29
    'lemma "(0::real) < x ==> 0 < y ==> y < 1 ==> x + y^150 > x * y^150"', #30
    'lemma "(0::real) < x ==> -1 < y ==> y < 0 ==> x + (y + 1)^150 > x * (y + 1)^150"',     #31
    #lines 233
    ]

repolya_statements = [
    'lemma "(ALL (x::real) y. f(x + y) = f(x) + f(y)) ==> f(a + b) > (2::real) ==> f(c + d) > 2 ==>f(a + b + c + d) > 4"', #24
    'lemma "(ALL (x::real) y. f (x + y) = f x * f y) ==> f a > (2::real) ==> f b > 2 ==>f(a + b) > 4"', #25
    'lemma "(0::real) <= n ==> n < (K / 2) * x ==> 0 < C ==> 0 < eps ==> eps < 1 ==> (1 + eps / (3 * (C + 3))) * n < K * x"',   #26
    'lemma "(0::real) < x ==> x < y ==> (1 + x^2) / (2 + y)^17 < (1 + y^2) / (2 + x)^10"', #27
    'lemma "(0::real) < x ==> x < y ==> (1 + x^2) / (2 + exp y) < (1 + y^2) / (2 + exp x)"', #28
    'lemma "(0::real) < x ==> 0 < y ==> y < 1 ==> x + y > x * y"', #29
    'lemma "(0::real) < x ==> 0 < y ==> y < 1 ==> x + y^150 > x * y^150"', #30
    'lemma "(0::real) < x ==> -1 < y ==> y < 0 ==> x + (y + 1)^150 > x * (y + 1)^150"',     #31
]

polya_statements_1_2=[
    'lemma "(0::real) < u ==> u < v ==> v < 1 ==> 2 <= x ==> x <= y ==> 2 * u * v^2 < v * y^2"',
    'lemma "(0 :: real) < 1 + y^2"',
    'lemma "(1::real) < x ==> (1 + y^2) * x > (1 + y^2)"',
    'lemma "(0::real) < x ==> x < 1 ==> 1 / (1 - x) > 1 / (1 - x^2)"',
    'lemma "(0::real) < u ==> u < v ==> 0 < z ==> z + 1 < w ==> (u + v + w)^3 < (u + v + w + 1)^5"',
    'lemma "(0::real) < u ==> u < v ==> 0 < z ==> z + 1 < w ==> (u + v + w)^33 < (u + v + w + 1)^55"',
    'lemma "(0::real) < u ==> u < (v^2 + 23)^3 ==> 0 < z ==> z + 1 < w ==> (u + (v^2 + 23)^3 + w)^3 < (u + (v^2 + 23)^3 + w + 1)^5"',
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> (x::real) <= y ==> u + f x < v + f y"',
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> 1 < v ==> (x::real) <= y ==> f x + u < v^2 + f y"',
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> 1 < w ==> 2 < s ==> (w + s) / 3 < v ==> (x::real) <= y ==> f x + u < v^2 + f y"',
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> 1 < v ==> (x::real) <= y ==> f x + u < (1 + v)^10 + f y"',
    'lemma "(ALL x. f x <= 1) ==> (0::real) < w ==> u < v ==> u + w * f x < v + w"'
    'lemma "(ALL x. f x <= 2) ==> (0::real) < w ==> u < v ==> u + w * (f x - 1) < v + w"',
    'lemma "(z :: real) > exp x \<Longrightarrow> w > exp y \<Longrightarrow> z^3 * w^2 > exp (3 * x + 2 * y)"',
    'lemma "(u::real) > 0 \<Longrightarrow> v > 0 \<Longrightarrow> x > 0 \<Longrightarrow> ln x > 2 * u + v \<Longrightarrow> x > 1"',
    'lemma "(x :: real) < y \<Longrightarrow> u \<le> v \<Longrightarrow> u + min (x + 2 * u) (y + 2 * v) \<le> x + 3 * v"',
]



polya_statements_1_4=[
    'lemma "(0::real) < u ==> u < v ==> v < 1 ==> 2 <= x ==> x <= y ==> 2 * u * v^2 < v * y^2"',
    'lemma "(0 :: real) < 1 + y^2"',
    'lemma "(1::real) < x ==> (1 + y^2) * x > (1 + y^2)"',
    'lemma "(0::real) < x ==> x < 1 ==> 1 / (1 - x) > 1 / (1 - x^2)"',
    'lemma "(0::real) < u ==> u < v ==> 0 < z ==> z + 1 < w ==> (u + v + w)^3 < (u + v + w + 1)^5"',
    'lemma "(0::real) < u ==> u < v ==> 0 < z ==> z + 1 < w ==> (u + v + w)^33 < (u + v + w + 1)^55"',
    'lemma "(0::real) < u ==> u < (v^2 + 23)^3 ==> 0 < z ==> z + 1 < w ==> (u + (v^2 + 23)^3 + w)^3 < (u + (v^2 + 23)^3 + w + 1)^5"',
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> (x::real) <= y ==> u + f x < v + f y"',
]

polya_statements_2_4=[
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> 1 < v ==> (x::real) <= y ==> f x + u < v^2 + f y"',
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> 1 < w ==> 2 < s ==> (w + s) / 3 < v ==> (x::real) <= y ==> f x + u < v^2 + f y"',
    'lemma "(ALL x y. x <= y --> f x <= f y) ==> (u::real) < v ==> 1 < v ==> (x::real) <= y ==> f x + u < (1 + v)^10 + f y"',
    'lemma "(ALL x. f x <= 1) ==> (0::real) < w ==> u < v ==> u + w * f x < v + w"'
    'lemma "(ALL x. f x <= 2) ==> (0::real) < w ==> u < v ==> u + w * (f x - 1) < v + w"',
    'lemma "(z :: real) > exp x \<Longrightarrow> w > exp y \<Longrightarrow> z^3 * w^2 > exp (3 * x + 2 * y)"',
    'lemma "(u::real) > 0 \<Longrightarrow> v > 0 \<Longrightarrow> x > 0 \<Longrightarrow> ln x > 2 * u + v \<Longrightarrow> x > 1"',
    'lemma "(x :: real) < y \<Longrightarrow> u \<le> v \<Longrightarrow> u + min (x + 2 * u) (y + 2 * v) \<le> x + 3 * v"',]

polya_statements_1_8=[
    'lemma "(0::real) < u ==> u < v ==> v < 1 ==> 2 <= x ==> x <= y ==> 2 * u * v^2 < v * y^2"',
    'lemma "(0 :: real) < 1 + y^2"',
    'lemma "(1::real) < x ==> (1 + y^2) * x > (1 + y^2)"',
]

polya_statements_test=[
    'lemma "(0 :: real) < 1 + y^2"',
]

polya_statements_aux = [
    'lemma "(0::real) < x ==> x < y ==> u < v ==> 2 * u + exp (1 + x + x^4) <= 2 * v + exp (1 + y + y^4)"',
    'lemma "(0::real) < x ==> 3 < y ==> (u::real) < v ==>2 * u + exp 10 <= 2 * v + exp (1 + y^2)"',
    'lemma "(ALL (x::real) y. f(x + y) = f(x) + f(y)) ==> f(a + b) > (2::real) ==> f(c + d) > 2 ==>f(a + b + c + d) > 4"',
    'lemma "(ALL (x::real) y. f (x + y) = f x * f y) ==> f a > (2::real) ==> f b > 2 ==>f(a + b) > 4"',
    'lemma "(0::real) <= n ==> n < (K / 2) * x ==> 0 < C ==> 0 < eps ==> eps < 1 ==> (1 + eps / (3 * (C + 3))) * n < K * x"',
    'lemma "(0::real) < x ==> x < y ==> (1 + x^2) / (2 + y)^17 < (1 + y^2) / (2 + x)^10"',
    'lemma "(0::real) < x ==> x < y ==> (1 + x^2) / (2 + exp y) < (1 + y^2) / (2 + exp x)"',
    'lemma "(0::real) < x ==> 0 < y ==> y < 1 ==> x + y > x * y"',
    'lemma "(0::real) < x ==> 0 < y ==> y < 1 ==> x + y^150 > x * y^150"',
    'lemma "(0::real) < x ==> -1 < y ==> y < 0 ==> x + (y + 1)^150 > x * (y + 1)^150"',
    #lines 233
    ]

second_half = [
    'lemma "(0::real) <= n ==> n < (K / 2) * x ==> 0 < C ==> 0 < eps ==> eps < 1 ==> (1 + eps / (3 * (C + 3))) * n < K * x"',
    'lemma "(0::real) < x ==> x < y ==> (1 + x^2) / (2 + y)^17 < (1 + y^2) / (2 + x)^10"',
    'lemma "(0::real) < x ==> x < y ==> (1 + x^2) / (2 + exp y) < (1 + y^2) / (2 + exp x)"',
    'lemma "(0::real) < x ==> 0 < y ==> y < 1 ==> x + y > x * y"',
    'lemma "(0::real) < x ==> 0 < y ==> y < 1 ==> x + y^150 > x * y^150"',
    'lemma "(0::real) < x ==> -1 < y ==> y < 0 ==> x + (y + 1)^150 > x * (y + 1)^150"',]