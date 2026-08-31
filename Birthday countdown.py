import calendar
import datetime
import sys
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
today = datetime.datetime(current_year, current_month, current_day)

print('=' * 30)
print('Birthday Countdown'.center(30))
print('=' * 30)
while True:
    while True:
        try:
            month = int(input('Which month were you born in: ').strip())
            if month < 1 or month > 12:
                print('\033[31mError, Invalid month!\033[m')
                continue

            break

        except ValueError:
            print('\033[31mERROR,Please enter only whole numbers!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mClosing program...\033[m')
            sys.exit()

    while True:
        try:
            year = int(input('The year you were born: ').strip())
            if year < 1000 or year > current_year:
                print('\033[mInvalid year!\033[m')
                continue
            break
        except ValueError:
            print('\033[31mERROR,Please enter only whole numbers!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mClosing program...\033[m')
            sys.exit()


    while True:
        try:
            days_in_month = calendar.monthrange(year,month)[1]
            day = int(input('The day you were born: ').strip())
            if day < 1 or day > days_in_month:
                print('\033[31mInvalid Day!\033[m')
                continue
            break

        except ValueError:
            print('\033[31mERROR,Please enter only whole numbers!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mClosing program...\033[m')
            sys.exit()

    print(f'Your date of birth: {day}/{month}/{year}')

    if  month == current_month and day == current_day:
        age = current_year - year
        print('Your birthday is today! Congratulations!')
        print(f'And you turn {age} years old.')

    else:
        if month < current_month or (month == current_month and day < current_day):
            print()
            birthday_year = current_year + 1
            print('Your birthday has already passed this year.')
            print('Your next birthday will be next year.')
        else:
            birthday_year = current_year
            print('Your birthday has not happened yet this year.')
        birthday = datetime.datetime(birthday_year, month, day)
        days_left = birthday - today
        age = birthday_year - year
        days = days_left.days
        week_number= birthday.weekday()
        days_w = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        week = days_w[week_number]

        print(f'{days} Day{"s" if days != 1 else ""} until your birthday!')
        print(f'You will turn {age} years old!')
        print(f'You were born on a {week}!')

    while True:
        try:
            r = input('Do you want to go back to the main menu? [Y or N]: ').strip().upper()
        except KeyboardInterrupt:
            print('\033[31mClosing program...\033[m')
            sys.exit()
        if r == 'N':
            print('\033[31mClosing program...\033[m')
            sys.exit()
        elif r == 'Y':
            break
        else:
            print('\033[31mError, type only Y or N!\033[m')
            continue
