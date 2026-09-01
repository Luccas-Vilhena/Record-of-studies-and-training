import string
import random

def password_generator(size=12):
        safe_symbols = '!@#$%&*'
        char_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + safe_symbols
        return ''.join(random.choice(char_pool) for _ in range(size))

def password_validator(password) :
        lower_count = sum(1 for p in password if p.islower())
        upper_count = sum(1 for p in password if p.isupper())
        digit_count = sum(1 for p in password if p.isdigit())
        special_count = sum(1 for p in password if not p.isalnum())

        score = 0
        if len(password) >= 8:
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
            print(f'\033[31m{password} Is Weak Password!\033[m')
        elif score <= 4:
            print(f'\033[33m{password} Is Medium Password!\033[m')
        else:
            print(f'\033[32m{password} Is Strong Password!\033[m')

        return score
