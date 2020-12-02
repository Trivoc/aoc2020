from src import setup_day
import datetime

AUTO_DATE = True
MANUAL_YEAR = 2020
MANUAL_DAY = 1


def setup_for_day(year, day):
    input = setup_day.create_module(year, day)
    print(input)
# Press the green button in the gutter to run the script.



if AUTO_DATE:
    now = datetime.datetime.now()
    setup_for_day(now.year, now.day)
else :
    setup_for_day(MANUAL_YEAR, MANUAL_DAY)





