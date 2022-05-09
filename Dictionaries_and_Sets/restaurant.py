MENU = {'Sandwich': 10, 'Tea': 7, 'Salad': 9}

def restaurant():
    total = 0

    while True:
        order = input('Order: ').strip()

        if not order:
            break

        if order in MENU:
            price = MENU[order]
            total += priceprint(f'{order} is {price}, total is {total}.')

        else:
            print(f'We are fresh out of {order} today, sorry.')

    print(f'Your order is {total}')

restaurant()
