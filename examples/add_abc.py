from lambda_ex import xlambda

add = xlambda('a, b', """
    return a + b
""")

print(add(1, 2))  # -> 3
