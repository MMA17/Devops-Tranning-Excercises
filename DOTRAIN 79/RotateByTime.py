import logging, time
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter

logger = logging.getLogger('RotatingFileHandler')
logger.setLevel(logging.DEBUG)

handler = TimedRotatingFileHandler('out1.log', when="m", interval=1)
formatter = Formatter('%(message)s %(asctime)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

while True:
    logger.warning("Logging at ")
    time.sleep(0.5)