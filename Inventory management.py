from Utils import exceptions

print('='*41)
print('\033[32m' + 'Inventory Management'.center(41) + '\033[m')
print('='*41)
print('1 | Products')
print('2 | Add Product')
print('3 | Remove Product')

stock = []
while True:
    try:
        user_option = int(input('Enter what you want to do: ').strip())
    except ValueError:
        exceptions.invalid_menu_input()
        continue
    except KeyboardInterrupt:
        exceptions.close_program()

    if user_option == 1:
        print('-' * 41)
        print('Products in Stock'.center(41))
        print('-' * 41)

        if not stock:
            print('\033[31mERROR! No products in stock!\031[m')
            continue
        list_products =  ' , '.join(stock)
        print(f'{list_products}')

    elif user_option == 2:
        while True:
            try:
                product = input('Name Product: ').strip().capitalize()
            except KeyboardInterrupt:
                exceptions.close_program()

            if not product:
                exceptions.empty_product_name()
                continue

            if product.isdigit():
                exceptions.product_cant_be_a_number()
                continue

            stock.append(product)
            print(f'The product {product} was added successfully in stock!')
            break

    elif user_option == 3:
        print('=' * 40)
        print('Remove from inventory'.center(40))
        print('=' * 40)

        product_remove = input('Name of the product you wish to remove: ').strip().capitalize()

        if product_remove not in stock:
            print('ERROR! Product not found!')
        else:
                print(f'{stock}')
                while True:
                        try:
                            r = input('Do you want to remove it [Y or N]: ').strip().upper()

                        except KeyboardInterrupt:
                            exceptions.close_program()

                        if r == 'Y':
                            stock.remove(product_remove)
                            print(f'Product {product_remove} successfully removed!')
                            break
                        elif r == 'N':
                            break
                        else:
                            exceptions.valid_option()
                            continue


    else:
        exceptions.valid_option()
        continue