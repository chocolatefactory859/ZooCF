from logging_config import Logger

logger = Logger()


def retry_until_success(exception_to_catch: Exception):
    """
    Wrapper retries it until exception_to_catch is not raised
    :param exception_to_catch: Exception to catch in function
    :param func: Function to perform on
    """
    def decorator(func):
        def inner(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                except exception_to_catch:
                    logger.debug("Retrying running function")
        return inner
    return decorator
