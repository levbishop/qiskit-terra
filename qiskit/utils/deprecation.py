# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Deprecation utilities"""

import functools
import inspect
import warnings


def _filter_deprecation_warnings():
    """Apply filters to deprecation warnings.

    Force the `DeprecationWarning` warnings to be displayed for the qiskit
    module, overriding the system configuration as they are ignored by default
    [1] for end-users.

    [1] https://docs.python.org/3/library/warnings.html#default-warning-filters
    [2] https://www.python.org/dev/peps/pep-0565/
    """

    warnings.filterwarnings(
        "default", category=DeprecationWarning, module=r"^qiskit\.", append=False
    )


_filter_deprecation_warnings()


def deprecate_arguments(kwarg_map):
    """Decorator to automatically alias deprecated argument names and warn upon use."""

    def decorator(func):
        sig = inspect.signature(func)
        params = sig.parameters
        for kwarg in kwarg_map:
            if kwarg in params:
                raise NameError(
                    f"`{func.__qualname__}`: deprecated argument `{kwarg}`(old) -> "
                    f"`{kwarg_map[kwarg]}`(new): old is present in argument list."
                )
            if kwarg_map[kwarg] not in params or params[kwarg_map[kwarg]].kind not in [
                inspect.Parameter.KEYWORD_ONLY,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
            ]:
                raise NameError(
                    f"`{func.__qualname__}`: deprecated argument `{kwarg}`(old) -> "
                    f"`{kwarg_map[kwarg]}`(new): new is not a keyword argument in arg list."
                )

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if kwargs:
                _rename_kwargs(func.__qualname__, kwargs, kwarg_map)
            return func(*args, **kwargs)

        # pylint: disable=no-member
        if wrapper.__doc__:
            wrapper.__doc__ += f"\n\nDeprecated arguments:\n"
            wrapper.__doc__ += "\n".join(
                f"\t{kwarg}: replaced by {kwarg_map[kwarg]}" for kwarg in kwarg_map
            )
        return wrapper

    return decorator


def deprecate_function(msg, stacklevel=2):
    """Emit a warning prior to calling decorated function.

    Args:
        msg (str): Warning message to emit.
        stacklevel (int): The warning stackevel to use, defaults to 2.

    Returns:
        Callable: The decorated, deprecated callable.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(msg, DeprecationWarning, stacklevel=stacklevel)
            return func(*args, **kwargs)

        wrapper._warned = False
        return wrapper

    return decorator


def _rename_kwargs(func_name, kwargs, kwarg_map):
    for old_arg, new_arg in kwarg_map.items():
        if old_arg in kwargs:
            if new_arg in kwargs:
                raise TypeError(
                    "`{}`: received both `{}`(new) and `{}(deprecated)`.".format(
                        func_name, new_arg, old_arg
                    )
                )

            warnings.warn(
                "`{}`: keyword argument `{}` is deprecated and "
                "replaced with `{}`.".format(func_name, old_arg, new_arg),
                DeprecationWarning,
                stacklevel=3,
            )

            kwargs[new_arg] = kwargs.pop(old_arg)
