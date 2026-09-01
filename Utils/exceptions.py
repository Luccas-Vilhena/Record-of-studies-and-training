import sys

def close_program():
    print('\033[31mClosing program...\033[m')
    sys.exit()

def unexpected_error():
    print('\033[31mUnexpected error!\033[m')

def invalid_menu_input():
    print('\033[31mERROR,Just type numbers!\033[m')

def invalid_option():
    print('\033[31mERROR, Please type only one of the valid options!\033[m')

def empty_product_name():
    print("\033[31mERROR, Product name can't be empty!\033[m")

def product_cant_be_a_number():
    print("\033[31mERROR, the product can't be a number!\033[m")
