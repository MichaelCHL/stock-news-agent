import logging
import os
import datetime

LOG_DIRS = 'logs'
os.makedirs(LOG_DIRS, exist_ok=True)
format = '%(asctime)s - %(levelname)s: %(message)s'

logging.basicConfig(
    filename=os.path.join(LOG_DIRS, datetime.datetime.now().strftime('log_%Y-%m-%d.log')),
    level=logging.DEBUG,
    # format=format 
)



def get_logger(name):
    logger = logging.getLogger(name)
    logger.propagate = False

    if not logger.handlers:
        # add logging to terminal
        st_handler = logging.StreamHandler()
        StreamHandlerformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        st_handler.setFormatter(StreamHandlerformatter)
        logger.addHandler(st_handler)

        file_handler = logging.FileHandler(filename=os.path.join(LOG_DIRS, datetime.datetime.now().strftime('log_%Y-%m-%d.log')),
)
        FileHandlerformatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(FileHandlerformatter)
        logger.addHandler(file_handler)

    return logging.getLogger(name)

if __name__ == "__main__":
    logger = get_logger("test")
    logger.info("first call")
    
    logger = get_logger("test")
    logger.info("second call")