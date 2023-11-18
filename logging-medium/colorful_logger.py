import logging
import colorlog

logger = logging.getLogger('TEST')
logger.setLevel(logging.DEBUG)

handle = logging.StreamHandler()
handle.setLevel(logging.DEBUG)
fmt = colorlog.ColoredFormatter(
    "%(name)s: %(white)s%(asctime)s%(reset)s %(log_color)s%(levelname)s%(reset)s %(process)d >>> %(log_color)s%(message)s%(reset)s"
)
handle.setFormatter(fmt)
logger.addHandler(handle)

logger.error("ERROR")
logger.info("INFO")