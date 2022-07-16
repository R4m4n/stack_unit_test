import logging, sys

class Logger():
    """
    Custom Logger class logs messages passed to it in the terminal.
    Has two functions according to requirement:
    info(message)
    error(message)
    """
    logger = logging.getLogger()
    logger.level = logging.NOTSET
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)

    @classmethod
    def info(cls, message):
        try:
            logging.getLogger().info(message)
        finally:
            cls.logger.removeHandler(cls.stream_handler)


    @classmethod
    def error(cls, message):
        try:
            logging.getLogger().error(message)
        finally:
            cls.logger.removeHandler(cls.stream_handler)