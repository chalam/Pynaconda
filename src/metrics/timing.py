# https://numericalrecipes.wordpress.com/2009/05/25/signature-preserving-function-decorators/

from __future__ import division

import inspect
import time
from os import name as OP_SYS


def performance_timer_2(_func_):
    """
    A decorator function to time execution of a function.

    Timing is activated by setting the verbose keyword to True.
    """

    stopwatch = time.time
    if OP_SYS in ('nt', 'dos'):
        stopwatch = time.clock

    def _wrap_(*args, **kwargs):
        """
        This is a function wrapper.
        """

        verbose = kwargs.pop('verbose', False)
        t = stopwatch()
        ret = _func_(*args, **kwargs)
        t = stopwatch() - t
        if verbose:
            print("Call to", _func_.__name__, "took", t, "sec.")
        return ret

    _wrap_.__name__ = _func_.__name__
    _wrap_.__doc__ = _func_.__doc__
    return _wrap_


def performance_timer_3(_func_):
    """
    A decorator function to time execution of a function.

    Timing is activated by setting the verbose keyword to True.
    """

    stopwatch = time.time
    if OP_SYS in ('nt', 'dos'):
        stopwatch = time.clock

    def _wrap_(*args, **kwargs):
        """
        This is a function wrapper.
        """

        verbose = kwargs.pop('verbose', False)
        t = stopwatch()
        ret = _func_(*args, **kwargs)
        t = stopwatch() - t
        if verbose:
            print("Call to", _func_.__name__, "took", t, "sec.")
        return ret

    sig = list(inspect.getargspec(_func_))
    wrap_sig = list(inspect.getargspec(_wrap_))
    if not sig[2]:
        sig[2] = wrap_sig[2]
    src = 'def %s%s :\n' % (_func_.__name__, inspect.formatargspec(*sig))
    src += '    return _wrap_%s\n' % (inspect.formatargspec(*sig))
    evaldict = {'_wrap_': _wrap_}
    exec(src in evaldict)
    ret = evaldict[_func_.__name__]
    ret.__doc__ = _func_.__doc__
    return ret


def signature_decorator(_wrap_, has_kwargs=False):
    """
    A decorator to create signature preserving wrappers.

    _wrap_     : the wrapper function, which must take a function as first
                 argument, can then take several optional arguments, which
                 must have defaults, plus the *args and **kwargs to pass to
                 the wrapped function.
    has_kwargs : should be set to True if the wrapper also accepts keyword
                 arguments to alter operation.
    """

    def decorator(func):
        """
        An intermediate decorator function
        """
        sig = list(inspect.getargspec(func))
        wrap_sig = list(inspect.getargspec(_wrap_))
        sig[0], wrap_sig[0] = sig[0] + wrap_sig[0][1:], wrap_sig[0] + sig[0]
        wrap_sig[0][0] = '_func_'
        sig[3] = list(sig[3]) if sig[3] is not None else []
        sig[3] += list(wrap_sig[3]) if wrap_sig[3] is not None else []
        sig[3] = tuple(sig[3]) if sig[3] else None
        wrap_sig[3] = None
        if sig[2] is None and has_kwargs:
            sig[2] = wrap_sig[2]
        wrap_sig[1:3] = sig[1:3]
        src = 'def %s%s :\n' % (func.__name__, inspect.formatargspec(*sig))
        src += '    return _wrap_%s\n' % (inspect.formatargspec(*wrap_sig))
        evaldict = {'_func_': func, '_wrap_': _wrap_}
        exec(src in evaldict)
        ret = evaldict[func.__name__]
        ret.__doc__ = func.__doc__
        return ret

    return decorator


def timer_wrapper_1(_func_, verbose=False, *args, **kwargs):
    """
    A wrapper to time functions, activated by the last argument.

    For use with signature_decorator
    """
    stopwatch = time.time
    if OP_SYS in ('nt', 'dos'):
        stopwatch = time.clock
    t = stopwatch()
    ret = _func_(*args, **kwargs)
    t = stopwatch() - t
    if verbose:
        print("Call to", _func_.__name__, "took", t, "sec.")
    return ret


def timer_wrapper_2(_func_, *args, **kwargs):
    """
    A wrapper to time functions, activated by a keyword argument..

    For use with signature_decorator
    """
    stopwatch = time.time
    if OP_SYS in ('nt', 'dos'):
        stopwatch = time.clock
    verbose = kwargs.pop('verbose', False)
    t = stopwatch()
    ret = func(*args, **kwargs)
    t = stopwatch() - t
    if verbose:
        print("Call to", _func_.__name__, "took", t, "sec.")
    return ret

def basic_stats(data):
    """
    Given a list of numbers, returns a dicitonary with the minimum, maximum,
    average and standard deviation, computed using Welford's method.

    """

    n = len(data)
    ret = {}
    if not n:
        ret['min'] = ret['max'] = ret['avg'] = ret['st_dev'] = None
    else:
        ret['min'] = min(data)
        ret['max'] = max(data)
        avg = data[0]
        var = 0
        for k, x in enumerate(data[1:], 2):
            delta = x - avg
            avg += delta / k
            var += delta * (x - avg)
        ret['avg'] = avg
        ret['st_dev'] = var ** (1 / 2) if n > 1 else None
    return ret


def performance_timer(_func_):
    """
    Decorator function to time execution of a function.

    Activated using the decorated function's **kwargs:

      verbose=1     --> Activates timing and printout
             =2     --> Increases output information
      timer_loops=1 --> Sets the number of times to run the function,
                        if gretaer than 1, output has detailed statistics

    """

    stopwatch = time.time
    if OP_SYS in ('nt', 'dos'):
        stopwatch = time.clock

    def _wrap_(*args, **kwargs):
        verbose = kwargs.pop('verbose', False)
        timer_loops = int(kwargs.pop('timer_loops', 1))
        if not verbose or timer_loops < 1:
            timer_loops = 1
        times = []
        ret = None
        for loop in range(timer_loops):
            times += [stopwatch()]
            ret = _func_(*args, **kwargs)
            times[-1] = stopwatch() - times[-1]
        if verbose:
            print("Call to", _func_.__name__,)
            if verbose > 1 and (args or kwargs):
                print("with arguments",)
                if args:
                    print(args,)
                if kwargs:
                    print(kwargs,)
            if timer_loops == 1:
                print("took %g sec." % (times[0]))
            else:
                print("took:")
                stats = basic_stats(times)
                for item in ('min', 'max', 'avg', 'st_dev'):
                    print("%g sec. (%s)" % (stats[item], item))
        return ret

    sig = list(inspect.getargspec(_func_))
    wrap_sig = list(inspect.getargspec(_wrap_))
    if not sig[2]:
        sig[2] = wrap_sig[2]
    src = 'def %s%s :\n' % (_func_.__name__, inspect.formatargspec(*sig))
    sig[3] = None  # if not, all vars with defaults are set to default value
    src += '    return _wrap_%s\n' % (inspect.formatargspec(*sig))
    evaldict = {'_wrap_': _wrap_}
    code = compile(src, '<string>', 'single')
    for code in evaldict:
        exec(code)
        ret = evaldict[_func_.__name__]
        ret.__doc__ = _func_.__doc__
    return ret

@performance_timer(timer_wrapper_1)
def decorated_sum(a,b=2) :
    """
    This is a function.
    """
    return a+b

if __name__ == '__main__':
    decorated_sum(1, 2)