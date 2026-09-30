import random as r

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*"
password = []

for i in range(3):
    password.append(r.choice(letters))

for i in range(3):
    password.append(r.choice(digits))

for i in range(2):
    password.append(r.choice(symbols))

print(''.join(password))

