roman_trans = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def convert_arabian_to_roman(number):
    result = ""
    for digit, roman in roman_trans:
        while number >= digit:
            result += roman
            number -= digit
    return result


def convert_roman_to_arabian(roman):
    digit_trans = {"I": 1, "V": 5, "X": 10, "L": 50,
              "C": 100, "D": 500, "M": 1000}

    total = 0
    for i in range(len(roman)):
        current = digit_trans[roman[i]]
        if i + 1 < len(roman) and current < digit_trans[roman[i + 1]]:
            total -= current
        else:
            total += current
    return total


# Тесты из задания
r = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]

for i in r:
    print(convert_roman_to_arabian(i))

print()

n = [14, 5, 12, 20, 100, 110, 520]
for r in n:
    print(convert_arabian_to_roman(r))
