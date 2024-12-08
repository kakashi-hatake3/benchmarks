import logging
import platform

from src import json_cleaner
from src.json_to_table import json_to_table

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())

    data = json_cleaner.clear_benchmarks()
    print(json_to_table(data))


if __name__ == "__main__":
    main()
