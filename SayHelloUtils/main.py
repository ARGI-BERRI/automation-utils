from loguru import logger

from automation_utils.random_utils import today_date_str
from SayHelloUtils.config import SHUConfig


def main() -> None:
    """Entry point of this program, if this script is executed directly."""
    config = SHUConfig()
    logger.add(config.logs_dir / "{time}.log", retention=3)

    logger.info(today_date_str())
    say_hello("Aoi")


def say_hello(name: str) -> None:
    """Say hello to the given name.

    Args:
        name (str): The name to greet.

    """
    logger.info(f"Hello, {name}!")


if __name__ == "__main__":
    main()
