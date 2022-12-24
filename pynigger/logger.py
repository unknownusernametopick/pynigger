import os
import pytz
import logging
import datetime
from pytz import UnknownTimeZoneError


class Formatter(logging.Formatter):
    """Override logging.Formatter"""

    # Taken from https://stackoverflow.com/a/67241679

    def formatTime(self, record, datefmt):
        date = datetime.datetime.fromtimestamp(record.created, tz=pytz.UTC)
        try:
            timezone = os.environ.get("TIMEZONE")
            if not timezone:
                timezone = "Asia/Kolkata"
            date = date.astimezone(pytz.timezone(timezone))
        except UnknownTimeZoneError:
            print(
                "WARNING - The timezone you filled doesn't exist. Please correct it. Till then, Indian timezone (Asia/Kolkata) will be used."
            )
            date = date.astimezone(pytz.timezone("Asia/Kolkata"))
        soln = date.strftime(datefmt)
        return soln


logger = logging.getLogger("ger_log")
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s",
                      "%Y-%m-%d %H:%M:%S")
console.setFormatter(formatter)
logger.addHandler(console)
logger.propagate = False
