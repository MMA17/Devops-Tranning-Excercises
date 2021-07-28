import logging, time
from logging.handlers import RotatingFileHandler
from logging import Formatter
#logging.basicConfig(format='%(message)s %(asctime)s', filename='./out.log' ,level=logging.DEBUG)
logger = logging.getLogger('RotatingFileHandler')
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler('out.log', maxBytes=1048576)
formatter = Formatter('%(message)s %(asctime)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

while True:
    logger.warning("Logging at ")
    time.sleep(0.5)

