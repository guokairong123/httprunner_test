import time
import uuid

from httprunner import __version__
from httprunner.response import  ResponseObject

def get_random_requset_id():
    requset_id = str(uuid.uuid4())
    return requset_id


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_folders_num(resp: ResponseObject) -> int:
    resp_json = resp.resp_obj.json()
    folders_num = len(resp_json["data"]["folders"])
    print(f"folders_num-------{folders_num}")
    return folders_num
