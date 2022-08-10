from lambda_ex import xlambda

fib = xlambda('n: int', """
    if n <= 0:
        raise ValueError(n)
    if n <= 2:
        return 1
    return __selfunc__(n - 1) + __selfunc__(n - 2)
""")

print(fib(10))
