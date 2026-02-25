import logging
import sys

from singleton.singleton_meta import SingletonMeta


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.setup_logging()
        self.logger = logging.getLogger("main logger")

    def setup_logging(self, level=logging.INFO):
        """
               Configure logging
        """
        logging.basicConfig(
            level=level,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            filename="zoo.log",
            filemode="a",
        )

    def get_logger(self):
        return self.logger

logger = Logger()

