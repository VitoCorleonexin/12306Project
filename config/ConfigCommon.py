import time
import os


def dec_make_dir(func):
    def handle_func(*args, **kwargs):
        dir_name = func(*args, **kwargs)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        elif not os.path.isdir(dir_name):
            pass
        return dir_name

    return handle_func


@dec_make_dir
def get_log_dir():
    return os.path.join(get_work_dir(), "tmp")


def get_work_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_now_time_stamp():
    return time.time()
