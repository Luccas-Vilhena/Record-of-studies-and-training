import sys

print('-' * 40)
print('Calculator IMC'.center(40))
print('-' * 40)
while True:
    while True:
        try:
            weight = float(input('Enter your weight: ').strip())
            if weight <= 0:
                print('\033[31mERROR, weight must be greater than zero!\033[m')
                continue
        except ValueError:
            print('\033[31mERROR, Please type numbers only!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mProgram interrupted by user.\033[m')
            sys.exit()
        except Exception as e:
            print(f'\033[31mUnexpected error: {e}\033[m')
            continue
        break

    while True:
        try:
            height = float(input('Enter your height: ').strip())
            if height <= 0:
                print('\033[31mERROR, height must be greater than zero!\033[m')
                continue
        except ValueError:
            print('\033[31mERROR, Please type numbers only!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mProgram interrupted by user.\033[m')
            sys.exit()
        except Exception as e:
            print(f'\033[31mUnexpected error: {e}\033[m')
            continue
        break

    imc = weight / (height ** 2)
    print(f'\033[33mYour IMC is: {imc:.2f}\033[m')

    if imc < 18.5:
        classification = 'Underweight'
    elif imc < 25:
        classification = 'Normal weight'
    elif imc < 30:
        classification = 'Overweight'
    elif imc < 35:
        classification = 'Obesity grade I'
    elif imc < 40:
        classification = 'Obesity grade II'
    else:
        classification = 'Obesity grade III'
    print(f'\033[33mClassification is : {classification}\033[m')

    r = input('\nCalculate again? [Y/n]: ').strip().lower()
    if r != 'y':
        break