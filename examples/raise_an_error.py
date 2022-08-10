from lambda_ex import xlambda

err = xlambda('', """
    return 2 / 0
""")

err()
