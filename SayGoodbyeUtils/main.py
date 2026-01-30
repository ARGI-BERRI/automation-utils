from loguru import logger

from automation_utils.best_utils import today_date_str


def main() -> None:
    """Entry point of this program, if this script is executed directly."""
    logger.add(__file__ + "/../logs/{time}.log", retention=3)

    logger.info(today_date_str())
    say_goodbye("Aoi")


def say_goodbye(name: str) -> None:
    """Say goodbye to the given name.

    Args:
        name (str): The name to greet.

    """
    logger.info(name)


if __name__ == "__main__":
    main()
