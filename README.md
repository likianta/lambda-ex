# lambda-ex

python lambda expression in multiple lines.

## install

```shell
pip install git+https://github.com/likianta/lambda-ex
```

## usage

```python
from lambda_ex import xlambda

add = xlambda('a, b', """
    return a + b
""")

print(add(1, 2))  # -> 3
```

### kwargs

```python
from lambda_ex import xlambda

add = xlambda('a, b, c=0', """
    return a + b + c
""")

print(add(1, 2))  # -> 3
print(add(1, 2, 3))  # -> 6
print(add(a=1, b=2, c=3))  # -> 6
```

if you are passing a complex object, for example a long list, you can also use
"post" kwargs as `xlambda`s third argument:

```python
from lambda_ex import xlambda

print_names = xlambda('title_case=False', """
    for n in names:
        if title_case:
            print(n.title())
        else:
            print(n)
""", kwargs={
    'names': (
        'anne',
        'bob',
        'charlie',
        'david',
        'erin',
    )
})

print_names(title_case=True)
#   -> Anne
#      Bob
#      Charlie
#      David
#      Erin
print_names(title_case=True, names=('fred', 'george', 'harry'))
#   -> Fred
#      George
#      Harry
```

### type annotations

```python
from lambda_ex import xlambda

add = xlambda('a: int, b: int', """
    return a + b
""")

print(add(1, 2))  # -> 3
```

### recursive call

use `__selfunc__` to call itself:

```python
from lambda_ex import xlambda

fibonacci = xlambda(('n'), """
    if n <= 0:
        raise ValueError(n)
    if n <= 2:
        return 1
    return __selfunc__(n - 1) + __selfunc__(n - 2)
""")

fibonacci(10)  # -> 55
```

### context (locals and globals)

lambda-ex can directly access locals and globals in its occurrence:

```python
from lambda_ex import xlambda

a = 1
b = 2

add = xlambda('', """
    return a + b
""")

add()  # -> 3
```

and modify local values:

```python
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
```

it equals to:

```python
a = 1
b = 2
c = 0

def __selfunc__():
    global c
    c = 3
    return a + b + c

add = __selfunc__

print(add())  # -> 6
print(a, b, c)  # -> 1 2 3
```

## tips & tricks

-   please check `examples` folder to get more usages.

-   if you're using pycharm, you can add a code template to pycharm's live
    template:

    ```
    xlambda('$END$', """

    """)
    ```

## cautions & limitations

-   use '\\n' instead of '\n' in your lambda expression. or you may use the
    r-string.

-   you cannot use `nonlocal` in xlambda. the `locals()` inside `__selfunc__`
    is an empty dict.
