import logging

def log_method_call(func):
    def wrapper(*args, **kwargs):
        logging.debug(f"Calling method: {func.__name__} with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.debug(f"Method: {func.__name__} returned: {result}")
        return result
    return wrapper
