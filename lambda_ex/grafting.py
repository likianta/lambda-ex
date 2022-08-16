from functools import partial
from typing import Callable

_grafted = set()


class TARGET:
    pass


def grafting(trigger: Callable, *args, one_off=True, **kwargs) -> Callable:
    """
    a handy implementation for "one-off" used decorator.

    classic usage:
        from lambda_ex import grafting
        @grafting(button.clicked.connect)
        def on_clicked():
            print('clicked')
    """
    
    def decorator(func):
        if one_off and (uid := (id(trigger), id(func))) in _grafted:
            return
        else:
            _grafted.add(uid)
        trigger(partial(func, *args, **kwargs))
        return func
    
    return decorator
