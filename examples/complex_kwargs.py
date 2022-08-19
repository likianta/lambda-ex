import lambda_ex

print(lambda_ex.__version__)

from lambda_ex import xlambda


class Foo:
    pass


bar = xlambda('a, b, c', """
    print(a, b, c, d)
""", kwargs={'d': Foo()})

bar(1, 2, 3)
