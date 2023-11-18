import logging

def test_logging():
    logging.basicConfig(level=logging.DEBUG)

    logging.debug("DEBUG")
    logging.info("INFO")
    logging.warning("WARNING")
    logging.error("ERROR")
    logging.critical("CRITICAL")

test_logging()