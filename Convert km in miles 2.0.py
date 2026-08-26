print('-'*30)
print('Km/miles converter'.center(30))
print('-'*30)
while True:
    while True:
        print('1| Convert km to miles')
        print('2| Convert miles to km')
        try:
            opcao = int(input('Which unit of distance do you want to convert to: ').strip())
        except ValueError:
            print('\033[31mERROR, Type only 1 or 2 in the options menu\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mERROR, No option provided\033[m')
            continue

        if opcao == 1:
            print('-' * 30)
            print('Convert km to miles')
            print('-' * 30)
            try:
                km_input = float(input('how many km: ').strip())
            except ValueError:
                print('\033[31mERROR, Please type a valid number for km\033[m')
                continue
            miles_result = km_input * 0.6214
            print(f'{km_input:.2f} Km converted to miles is {miles_result:.2f} miles.')
            break

        elif opcao == 2:
            print('-' * 30)
            print('Convert miles to km')
            print('-' * 30)
            try:
                miles_input = float(input('How many miles: ').strip())
            except ValueError:
                print('\033[31mERROR, Please type a valid number for miles\033[m')
                continue
            km_result = miles_input * 1.60934
            print(f'{miles_input:.2f} Miles converted to km is {km_result:.2f} km.')
            break

        else:
            print('\033[31mERROR,Enter only one of the two valid options!\033[m')
    print('Do you want to continue?')
    r = input('Yes or no: ').strip().lower()
    if r == 'no':
        break
    elif r == 'yes':
        pass
    else:
        while True:
            print('ERROR, Enter only yes or no!')
            r = input('Yes or no: ').strip().lower()
            if r == 'yes' or r == 'no':
                break
    if r == 'no':
        break