import logging

from singleton.singleton_meta import SingletonMeta


class Logger(metaclass=SingletonMeta):
    def __init__(self, level=logging.INFO):
        self.setup_logging(level)
        self.logger = logging.getLogger("main logger")

    def setup_logging(self, level):
        """
        Configure logging
        """
        logging.basicConfig(
            level=level,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            filename="zoo.log",
            filemode="a",
        )

    def __getattr__(self, name):
        """
        Delegate attribute access to the internal logger.
        """
        return getattr(self.logger, name)
