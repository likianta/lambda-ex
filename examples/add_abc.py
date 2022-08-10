from lambda_ex import xlambda

add = xlambda('a, b', """
    return a + b
""")

print('demo1:', add(1, 2))  # -> 3

# -----------------------------------------------------------------------------

a = 1
b = 2
c = 0

add = xlambda('', """
    global c
    c = 3
    return a + b + c
""")

print('demo2:', add())  # -> 6
print('demo2:', a, b, c)  # -> 1 2 3
