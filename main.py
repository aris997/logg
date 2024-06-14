import os
import time
import locale
import logging

import utils as u

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

# LOG
LOG_DIR = os.path.join("logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

#max size of log file:
MAX_BYTES = 20_000_000   #20 MB 20_000_000
CUT_PCT = 0.75   #percentage of old logs to trim

formatter = logging.Formatter('%(levelname)s:    \033[96m%(asctime)s f=\033[94m%(funcName)s \033[95m%(filename)s:%(lineno)d \033[96m= %(message)s\033[0m', datefmt="%d %B %Y %H:%M:%S")
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
fname = f"logg{u.now()}.log"
LOG_PATH = os.path.join(LOG_DIR, fname)

# file_handler = logging.FileHandler(os.path.join(LOG_DIR, f"logg{u.now()}.log"), mode='a')
# file_handler = logging.handlers.TimedRotatingFileHandler(LOG_PATH, when="S", interval=1, backupCount=10, encoding="utf-8", delay=False)
file_handler = logging.handlers.RotatingFileHandler(LOG_PATH, mode='a', maxBytes=MAX_BYTES, backupCount=5, encoding="utf-8", delay=False)

formatter = logging.Formatter('%(levelname)s: %(asctime)s f=%(funcName)s %(filename)s:%(lineno)d = %(message)s', datefmt="%Y-%m-%d %H-%M-%S")
file_handler.setFormatter(formatter)
logger = logging.getLogger("logg")
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
logger.debug("Start logging...")

time.sleep(2)

logger.critical("Hello there")
logger.critical("Hello there")
logger.critical("Hello there")


def do_something():
    logger.critical("Hello there")
    for _ in range(100):
        logger.error("General Kenobi")

while True:
    logger.debug("start")
    do_something()