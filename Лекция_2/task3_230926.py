def print_pack_report(amount):
    for i in range(amount, 0, -1):
        if i % 5 == 0 and i % 3 == 0:
            print(f'{i} - расфасуем по 3 или по 5')
        elif i % 5 == 0 and i % 3 != 0:
            print(f'{i} - расфасуем по 5')
        elif i % 3 == 0 and i % 5 != 0:
            print(f'{i} - расфасуем по 3')
        else:
            print(f'{i} - не заказываем!')

print_pack_report(30)