import time


def wait(secs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            time.sleep(secs)
            return ret

        return wrapper

    return decorator
