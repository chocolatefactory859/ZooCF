import logging
import sys

from singleton.singleton_meta import SingletonMeta


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        """
        Configure logging
        """
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            stream=sys.stdout
        )
        self.logger = logging.getLogger("main logger")

    def get_logger(self):
        return self.logger

logger = Logger()

