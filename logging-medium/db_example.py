import logging
from time import sleep

def db_connection(user: str, password: str, logger: logging.Logger) -> str:
    """
    Dummy database connection
    """
    conn_str = user + password
    logger.info("Connection started")
    sleep(1)
    try:
        conn = "Connection"
        logger.info("Connection succesfull")
    except:
        logger.error("Error during db connection")
    return conn

def send_data(data: tuple, conn: str, logger: logging.Logger) -> None:
    logger.info("Data sent")

def main():

    # prepare logger 
    logger = logging.getLogger('TEST')
    logger.setLevel(logging.DEBUG)
    handle = logging.StreamHandler()
    handle.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handle.setFormatter(formatter)
    logger.addHandler(handle)

    logger.info("Programm Started")
    sleep(1)
    
    conn = db_connection(user='test', password='test', logger=logger)

    data = ("test", 123)
    send_data(data=data, conn=conn, logger=logger)
main()