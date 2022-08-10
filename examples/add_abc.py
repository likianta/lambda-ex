from lambda_ex import xlambda

a = 1
b = 2
c = 0

add = xlambda('', """
    global c
    c = 3
    return a + b + c
""")

print(add())  # -> 6
print(a, b, c)  # -> 1 2 3


def foo():
    a = 1
    b = 2
    c = 4
    
    add = xlambda('', """
        # nonlocal c
        # c = 3
        return a + b + c
    """)
    
    print(add())  # -> 6
    print(a, b, c)  # -> 1 2 3


foo()
