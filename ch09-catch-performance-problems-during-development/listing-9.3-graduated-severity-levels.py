import functools
import time
import warnings

class PerformanceError(Exception):
    pass

def check_performance(
    func_name, duration_ms,
    warn_threshold_ms, error_threshold_ms,
    context=None
):
    if not __debug__:
        return
    if duration_ms > error_threshold_ms:
        msg = (
            f"CRITICAL: {func_name} took {duration_ms:.0f}ms"
            f" (error threshold: {error_threshold_ms}ms)"
        )
        if context:
            msg += f"\ncontext: {context}"
        print(msg, file=sys.stderr)
        raise PerformanceError(
            f"{func_name} exceeded {error_threshold_ms}ms threshold"
        )
    elif duration_ms > warn_threshold_ms:                                    #B
        msg = (
            f"WARNING: {func_name} took {duration_ms:.0f}ms"
            f" (warn threshold: {warn_threshold_ms}ms)"
        )
        if context:
            msg += f"\ncontext: {context}"
        warnings.warn(msg)

def assert_performance(warn_threshold_ms, error_threshold_ms, context_fn=None):  #C
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not __debug__:
                return func(*args, **kwargs)
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            context = context_fn(*args, **kwargs) if context_fn else None
            check_performance(
                func.__name__, duration,
                warn_threshold_ms, error_threshold_ms,
                context=context,
            )
            return result
        return wrapper
    return decorator

@assert_performance(                                                         #D
    warn_threshold_ms=160,
    error_threshold_ms=300,
    context_fn=lambda cart_items, user_id: {"cart_items": len(cart_items)},
)
def calculate_cart_total(cart_items, user_id):
    promotions = fetch_applicable_promotions(cart_items, user_id)
    subtotals = apply_promotions(cart_items, promotions)
    return sum(item.final_price for item in subtotals)
