#1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
#2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

import datetime

def print_days():
    one_day = datetime.timedelta(days=1)
    thirty_days = datetime.timedelta(days=30)
    today = datetime.date.today()
    yesterday = today - one_day
    month_ago = today - thirty_days
    print(today)
    print(yesterday)
    print(month_ago)

def str_2_datetime(date_string):
    day = datetime.datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return day 

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
