#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

from datetime import timedelta
from functools import wraps
from timeit import default_timer as timer
from typing import Any, Callable, Optional


def metrics(func: Optional[Callable] = None, name: Optional[str] = None, hms: Optional[bool] = False) -> Any:
    """Decorator to show execution time.

    :param func: Decorated function
    :param name: Metrics name
    :param hms: Show as human-readable string
    """
    assert callable(func) or func is None

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            comment = f"Execution time of {name or fn.__name__}:"
            t = timer()
            result = fn(*args, **kwargs)
            te = timer() - t

            # Log metrics
            from common import log
            logger = log.withPrefix('[METRICS]')
            if hms:
                logger.info(f"{comment} {timedelta(seconds=te)}")
            else:
                logger.info(f"{comment} {te:>.6f} sec")

            return result
        return wrapper

    return decorator(func) if callable(func) else decorator
