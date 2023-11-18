import logging

def test_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s")

    for i in ["Dog", "Cat"]:
        logging.info("%s is your animal!", i)


test_logging()