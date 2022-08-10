from __future__ import annotations

from functools import partial
from inspect import currentframe
from textwrap import dedent
from textwrap import indent

_uid = 0  # simple incremental id generator.


def xlambda(args: str, code_block: str, inherit_context=True, *,
            kwargs: dict = None, selfunc_name='__selfunc__'):
    global _uid
    _uid += 1
    hook_key = f'__anonymous_func_{_uid}__'
    
    params = _prepare_params(args, kwargs)
    
    caller_frame = currentframe().f_back
    context_g, context_l = _get_context(caller_frame, inherit_context)
    
    code_wrapper = dedent('''
        def {selfunc}({params}):
            try:
                {source_code}
            except Exception as e:
                raise InnerError(e)
        {func_hook} = {selfunc}
    ''').format(
        file=context_g['__file__'],
        params=params,
        source_code=indent(dedent(code_block), ' ' * 8),
        func_hook=hook_key,
        selfunc=selfunc_name,
    )
    # print(code_wrapper)
    
    exec(code_wrapper, context_g, context_l)
    # print(context[hook_key])
    return context_l[hook_key]


def _prepare_params(args: str, kwargs: dict | None) -> str:
    if kwargs is None:
        return args
    else:
        out = args + ', ' + ', '.join(f'{k}={v}' for k, v in kwargs.items())
        return out.strip(', ')


def _get_context(frame, full: bool) -> tuple[dict, dict]:
    # print(frame.f_globals['__file__'])
    globals_ = frame.f_locals if full else {}
    locals_ = {
        'InnerError': partial(
            InnerError,
            file_source=frame.f_globals['__file__'],
            line_offset=frame.f_lineno,
        )
    }
    return globals_, locals_


class InnerError(Exception):
    
    def __init__(self, raw_error: Exception,
                 file_source: str, line_offset: int):
        # note: the border line is from `lib:rich.box.ROUNDED`.
        self._error = dedent('''
            ╭─────────────────────────────────────────────────────────────────╮
            │ There was an error happened in xlambda function.                │
            │ Here is the useful information for your diagnosis:              │
            │    Source: "{file}:{line}"
            │    Error: {error}
            ╰─────────────────────────────────────────────────────────────────╯
        ''').rstrip().format(
            file=file_source,
            line=(raw_error.__traceback__.tb_lineno - 3) + line_offset - 1,
            error=str(raw_error),
        )
    
    def __str__(self):
        return self._error
