import requests
import time

def retry(cooloff=5, exc_type=None):
    if not exc_type:
        exc_type = [requests.exceptions.ConnectionError]

    def real_decorator(function):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    if e.__class__ in exc_type:
                        print("failed (?)")
                        time.sleep(cooloff)
                    else:
                        raise e
        return wrapper
    return real_decorator