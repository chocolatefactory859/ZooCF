from contextlib import contextmanager

from logging_config import Logger
from toilet.toilet2 import Toilet2

logger = Logger()


class ToiletContext:
    @staticmethod
    @contextmanager
    def toilet_context(toilet_output_path: str) -> Toilet2:
        """
        Opens the toilet lid and redirects stdout to the toilet file
        Ensures the lid is closed even if an exception occurs

        param: toilet_output_path: Path to the toilet output file
        yield: Toilet2 instance
        """
        toilet = Toilet2(toilet_output_path)

        try:
            toilet.open_lid()
            yield toilet

        except Exception as exception:
            logger.error(f"Error occurred: {exception}")

        finally:
            toilet.close_lid()
