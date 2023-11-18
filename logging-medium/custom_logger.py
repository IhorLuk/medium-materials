import logging

logger = logging.getLogger('TEST')
logger.setLevel(logging.DEBUG)

handle = logging.StreamHandler()
handle.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handle.setFormatter(formatter)
logger.addHandler(handle)

logger.debug("DEBUG")
logger.info("INFO")