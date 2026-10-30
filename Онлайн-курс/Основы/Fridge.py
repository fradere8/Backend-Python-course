from datetime import date, datetime, timedelta
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date=None):
    amount_d = Decimal(str(amount))
    if expiration_date is not None:
        expiration_date = datetime.strptime(expiration_date, DATE_FORMAT).date()

    if title in items:
        items[title].append({'amount': amount_d, 'expiration_date': expiration_date})
    else:
        items[title] = [{'amount': amount_d, 'expiration_date': expiration_date}]


def add_by_note(items, note):
    note_str = note.split(' ')
    am_n = None
    name_n = None
    try:
        datetime.strptime(note_str[-1], DATE_FORMAT).date()
        am_n = note_str[-2]
        name_n = ' '.join(note_str[:-2])
        add(items, name_n, am_n, note_str[-1])
    except ValueError:
        am_n = Decimal(note_str[-1])
        name_n = ' '.join(note_str[:-1])
        add(items, name_n, am_n)
    

def find(items, needle):
    result = []
    for k in items:
        if needle.lower() in k.lower():
            result.append(k)
    return result


def get_amount(items, needle):
    product_amount = Decimal(0)
    items_by_needle = find(items, needle)
    for i in items_by_needle:
        for j in range(len(items[i])):
            product_amount += items[i][j]['amount']
    return product_amount


def get_expired(items, in_advance_days=0):
    current_date = date.today()
    exp_d = current_date + timedelta(days=in_advance_days)
    result = []
    for key, parts in items.items():
        amount = Decimal(0)
        for part in parts:
            e_date = part['expiration_date']
            if e_date is not None and e_date <= exp_d:
                amount += part['amount']
        if amount > 0:
            result.append((key, amount))
    return result


goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': date(2023, 7, 15)},
        {'amount': Decimal('2.0'), 'expiration_date': date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

add(goods, 'Молоко', 1.0, '2023-07-20')
add_by_note(goods, 'Сыр 0.3 2023-07-25')
add(goods, 'Молоко', 0.5, '2023-07-22')
find_result = find(goods, 'молоко')
amount_result = get_amount(goods, 'молоко')
result_expired = get_expired(goods, in_advance_days=5)

print("Find result:", find_result)
print("Amount result:", amount_result)
print("Expired products:", result_expired)