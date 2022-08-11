from functools import partial
from typing import Callable

_grafted = set()


def grafting(trigger: Callable, *args, singleton=True, **kwargs) -> Callable:
    """
    classic usage:
        from lambda_ex import grafting
        @grafting(button.clicked.connect)
        def on_clicked():
            print('clicked')
    """
    
    def decorator(func):
        if singleton:
            if (uid := (id(trigger), id(func))) not in _grafted:
                trigger(partial(func, *args, **kwargs))
                _grafted.add(uid)
        else:
            trigger(partial(func, *args, **kwargs))
        return func
    
    return decorator
