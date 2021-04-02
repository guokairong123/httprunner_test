import time
import uuid

from httprunner import __version__


def get_random_requset_id():
    requset_id = str(uuid.uuid4())
    return requset_id


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)
