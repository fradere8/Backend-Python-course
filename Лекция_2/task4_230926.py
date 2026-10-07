import random as rnd

lower_register = "abcdefghijklmnopqrstuvwxyz"
upper_register = lower_register.upper()
digits = "0123456789"
symbols = "!@#$%^&*()-_=+"


def generate_password(length, lower, upper, has_symbols, has_digits):
    characters = ""
    if lower == "д":
        characters += lower_register
    if upper == "д":
        characters += upper_register
    if has_symbols == "д":
        characters += symbols
    if has_digits == "д":
        characters += digits

    password = []

    for i in range(length):
        password.append(rnd.choice(characters))

    return ''.join(password)

length = int(input("Введите длину пароля: "))
lower = input("Нужен нижний регистр (д/н)?  ")
upper = input("Нужен верхний регистр (д/н)?  ")
has_symbols = input("Нужны спец. символы (д/н)?  ")
has_digits = input("Нужны цифры (д/н)?  ")

print(generate_password(length, lower, upper, has_symbols, has_digits))
