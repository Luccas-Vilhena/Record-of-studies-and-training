km_units = ['km', 'kilometers', 'kilometre', 'klick']
miles_units = ['miles', 'nautical miles', 'mileage', 'mileage plus']
while True:
    phrase = []
    numbers = []
    origin = None
    destiny = None
    repeat_unit = False
    print('-'*51)
    try:
        user_text = input('Enter the distance you want to convert to miles/km: ').strip().lower()
        if not user_text:
            print("\033[31mERROR,You didn't type anything!\033[m")
            continue

        for caractere in user_text.split():
            if caractere in km_units or caractere in miles_units:
                phrase.append(caractere)
                if origin is None:
                    origin = caractere
                elif destiny is None:
                    destiny = caractere
                else:
                    repeat_unit = True
            else:
                try:
                    float(caractere)
                    numbers.append(caractere)
                except ValueError:
                    pass
        if repeat_unit:
            print('\033[31mERROR: too many length units in the phrase!\033[m')
            continue
            
        if  origin is None:
            print('\033[31mERROR: No length unit recognized!\033[m')
            continue

        if (origin in km_units and destiny in km_units) or (origin in miles_units and destiny in miles_units):
            print('\033[31mERROR, the two units of length belong to the same category!\033[m')
            continue

        else:
            try:
                value = float(numbers[0])
            except IndexError:
                print('\033[31mERROR, no number was typed!\033[m')
                continue

            if origin in km_units:
                result = value * 0.6214
                print(f'{value:.2f} km converted to miles is {result:.2f} miles.')
            elif origin in miles_units:
                result = value * 1.60934
                print(f'{value:.2f} miles converted to km is {result:.2f} km.')

    except KeyboardInterrupt:
        print('\033[31mERROR,you need to enter something!\033[m')
    print('-'*51)
    print('Do you want to continue?')
    r = input('Yes or no: ').strip().lower()
    if r == 'no':
        break
    elif r == 'yes':
        pass
    else:
        while True:
            print('\033[31mERROR, Enter only yes or no!')
            r = input('Yes or no: ').strip().lower()
            if r == 'yes' or r == 'no':
                break
        if r == 'no':
            break