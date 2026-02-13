from loguru import logger

from automation_utils.random_utils import today_date_str
from SayGoodbyeUtils.config import SGUConfig


def main() -> None:
    """Entry point of this program, if this script is executed directly."""
    config = SGUConfig()
    logger.add(config.logs_dir / "{time}.log", retention=3)

    logger.info(today_date_str())
    say_goodbye("Aoi")


def say_goodbye(name: str) -> None:
    """Say goodbye to the given name.

    Args:
        name (str): The name to say goodbye to.

    """
    logger.info(f"Goodbye, {name}!")


if __name__ == "__main__":
    main()
