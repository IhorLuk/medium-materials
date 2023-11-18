import logging

def test_logging():
    logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="basic.log")

    logging.debug("DEBUG")
    logging.info("INFO")
    logging.warning("WARNING")
    logging.error("ERROR")
    logging.critical("CRITICAL")

test_logging()