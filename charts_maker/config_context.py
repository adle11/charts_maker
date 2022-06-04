import configparser
import logging
import os
import time


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(ROOT_DIR, 'configs', 'configs.ini')
DEFAULT_LOGS_FILENAME = os.path.join(ROOT_DIR, 'porematgen.log')
DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'

current_config_file = CONFIG_FILE


def read_config(sections: tuple):
    if not os.path.exists(current_config_file):
        raise Exception(f"Config file {current_config_file} does not exists!")
    else:
        cp = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        cp.read(current_config_file, encoding='utf8')
        return tuple([cp[s] for s in sections])


def get_output_path():
    return read_config(sections=('common',))[0].get('output_data_dir', fallback='')


def get_datetime_str(time_struct=None):
    if time_struct is None:
        return time.strftime(DATETIME_FORMAT, time.localtime())
    else:
        return time.strftime(DATETIME_FORMAT, time_struct)


def get_logger(name, custom_logs_filename=None):
    formatter = logging.Formatter('%(asctime)s::%(name)s:%(lineno)d::%(levelname)s::%(message)s')

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages

    if custom_logs_filename is not None:
        fh = logging.FileHandler(os.path.join(ROOT_DIR, custom_logs_filename))
    else:
        fh = logging.FileHandler(os.path.join(ROOT_DIR, DEFAULT_LOGS_FILENAME))
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

