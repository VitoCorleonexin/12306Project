import os
import time
import logging
from config import ConfigCommon

logger = None
loggerHandler = None
date_str = ''
suffix = ''


def set_suffix(s):
    global suffix
    suffix = s


def get_today_date_str():
    return time.strftime("%Y-%m-%d", time.localtime(ConfigCommon.get_now_time_stamp()))


def set_date_str(s):
    global date_str
    date_str = s


def is_another_day(s):
    global date_str
    return date_str != s


def get_log_file():
    global date_str, suffix
    rtn = os.path.join(ConfigCommon.get_log_dir(), date_str)
    if suffix:
        rtn += "_" + suffix
    return rtn + ".log"


def log(msg, func='info'):
    global logger
    if not logger:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

    today_str = get_today_date_str()
    if is_another_day(today_str):
        set_date_str(today_str)
        logger.removeHandler(loggerHandler)

        fh = logging.FileHandler(get_log_file())
        fm = logging.Formatter(u"[%(asctime)s][%(levelname)8s] --- %(message)s "
                               "(%(filename)s:%(lineno)s)")
        fh.setFormatter(fm)

        logger.addHandler(fh)

        levels = {
            "debug": logger.debug,
            "info": logger.info,
            "warning": logger.warning,
            "error": logger.error,
            "critical": logger.critical

        }
        levels[func](msg)
