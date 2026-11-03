def factorialIterative(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

expectedFactorial = 362880
assert factorialIterative(9) == expectedFactorial