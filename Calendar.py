import calendar
from Utils import terminal
from datetime import datetime

terminal.print_header('Calendar', 20, 32)

today = datetime.now()

for week in calendar.monthcalendar(today.year,today.month):
    for day in week:
        if day == 0:
            print(f' ', end=' ')
        elif day == today.day:
            print(f'\033[31m{day}\033[m', end='')
        else:
            print(day, end=' ')
    print()