from time import sleep
from functools import wraps


def retry(exception, tries=4, delay=3, delay_multiplier=2):
    def do_retry(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            t, d = tries, delay
            while t > 1:
                try:
                    return f(*args, **kwargs)
                except exception as e:
                    print(f"{e}: retrying in {d} seconds..")

                    sleep(d)
                    t -= 1
                    d *= delay_multiplier
            return f(*args, **kwargs)

        return wrapper

    return do_retry


@retry(Exception)
def test():
    raise Exception("Fail")

test()
