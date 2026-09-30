text = input()
n = int(input())

ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
en = "abcdefghijklmnopqrstuvwxyz"

def get_language(text):
    is_ru = False
    is_en = False
    for char in text.lower():
        if char in ru:
            is_ru = True
        elif char in en:
            is_en = True

    if is_ru:
        return 'ru'
    if is_en:
        return 'en'
    else:
        return None

def encode(text, n):
    lang = get_language(text)
    alphabet = ''
    if lang == 'ru':
        alphabet = ru
    elif lang == 'en':
        alphabet = en
    else:
        return "строка не содержит ru/en букв"

    result =[]
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + n) % len(alphabet)
            result.append(alphabet[new_index])
        else:
            result.append(char)

    return ''.join(result)

def decode(text, n):
    return encode(text, -n)

c = encode(text, n)
print(c)

d = decode(c, n)
print(d)








