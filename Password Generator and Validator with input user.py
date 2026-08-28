import random
import string
from Utils.Password_validator.Validator import password_validator

safe_symbols = '!@#$%&*'
char_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + safe_symbols
print('-' * 30)
print('Password Generator'.center(30))
print('Validator Password'.center(30))
print('-' * 30)
print('1| Generate a password through the system')
print('2| Type your own password')
while True:
    reply = input('What do you want to do: ').strip()
    if reply != '1' and reply != '2':
        print('\033[31mERROR, Type only one of the two options!\033[m')
        continue
    if reply == '1':
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
            if lower_count > 0:
                score += 1
            if upper_count > 0:
                score += 1
            if digit_count > 0:
                score += 1
            if special_count > 0:
                score += 1

            if score <= 2:
                print(f'\033[31m{result} Is Weak Password!\033[m')
            elif score <= 4:
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
    elif reply == '2':
            password_user = input('Enter your password: ').strip()
            if not password_user:
                print('\033[31mERROR, Type something!\033[m')
                continue
            score = password_validator(password_user)
