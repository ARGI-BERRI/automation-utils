import datetime as dt
from zoneinfo import ZoneInfo


def today_date_str(tz: str = "Asia/Tokyo") -> str:
    """Get today's date string in the format `YYYY-MM-DD`.

    Args:
        tz (str, optional): Timezone name. Defaults to "Asia/Tokyo".

    Returns:
        str: Today's date string in the format `YYYY-MM-DD`.
    """
    return dt.datetime.now(tz=ZoneInfo(tz)).strftime("%Y-%m-%d")
