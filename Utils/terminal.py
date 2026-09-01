import os
from Utils import exceptions

def print_colored(text, color):
    print(f'\033[{color}m{text}\033[m')

def print_header(text,width,color):
    print('=' * width)
    print_colored(text.center(width), color)
    print('=' * width)

def pause(message='Press Enter to continue...'):
    input(message)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_valid_string(prompt):
    while True:
        try:
            value = input(prompt).strip()
        except KeyboardInterrupt:
            exceptions.close_program()
            continue
        if not value:
            exceptions.empty_product_name()
            continue
        return  value

def get_menu_choice(prompt, options):
    while True:
        choice = get_valid_int(prompt)

        if choice not in options:
            exceptions.invalid_option()
            continue
        return choice

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            exceptions.invalid_menu_input()

        except KeyboardInterrupt:
            exceptions.close_program()

def confirm_action(message):
    while True:
        try:
            r = input(message).strip().upper()
        except KeyboardInterrupt:
            exceptions.close_program()
            continue

        if r == 'Y':
            return True
        elif r == 'N':
            return False
        else:
            exceptions.invalid_option()

