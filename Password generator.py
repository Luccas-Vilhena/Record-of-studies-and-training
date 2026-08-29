import random
import string

safe_symbols = '!@#$%&*'
char_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + safe_symbols
while True:
    password_chars = []
    for char in range(12):
        random_char = random.choice(char_pool)
        password_chars.append(random_char)
    result = ''.join(password_chars)

    lower_count = 0
    upper_count = 0
    digit_count = 0
    special_count = 0
    score = 0

    for key in result:

        if key.islower():
            lower_count += 1
        elif key.isupper():
            upper_count += 1
        elif key.isdigit():
            digit_count += 1
        else:
            special_count += 1

    if len(result) >= 8:
        score += 1
    if len(result) >= 12:
        score += 1
    if lower_count > 2:
        score += 1
    if upper_count > 0:
        score += 1
    if digit_count > 0:
        score += 1
    if special_count > 0:
        score += 1

    print('-' * 30)
    print('Password Generator'.center(30))
    print('-' * 30)

    if score <= 3:
        print(f'\033[31m{result} Is Weak Password!\033[m')
    elif score <= 5:
        print(f'\033[33m{result} Is Medium Password!\033[m')
    else:
        print(f'\033[32m{result} Is Strong Password!\033[m')

    r = input('Do you want to continue [Yes or no]: ').strip().lower()
    if r == 'yes':
        pass
    elif r == 'no':
        break
    else:
        while True:
            print('\033[31mERROR, Type just yes or no!\033[m')
            r = input('Yes or no: ').strip().lower()
            if r == 'yes' or r == 'no':
                break
        if r == 'no':
            break