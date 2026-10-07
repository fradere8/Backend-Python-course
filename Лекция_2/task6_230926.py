import random as rnd

words = ["импрессионизм", "турбулентность", "пристрастие",
         "частота", "матрица", "благородие", "эмблема",
         "вестибюль", "мороженое"]

patterns = [1, 2, 3, 4, 5, 6, 7]
wrong_letters = []

word = rnd.choice(words)
guessed_letters = ["_"] * len(word)

while len(patterns) > 0:
    print(" ".join(guessed_letters))
    a = input("Ваша буква:  ").lower()

    if a in guessed_letters or a in wrong_letters:
        print("Эта буква уже была")
        continue

    if a in word:
        for i in range(len(word)):
            if word[i] == a:
                guessed_letters[i] = a

        if "_" not in guessed_letters:
            print("Вы выиграли! Слово:", word)
            break
    else:
        wrong_letters.append(a)
        del patterns[-1]
        print(f"Промах. Вы можете ошибиться еще {len(patterns)} раз")
else:
    print("Вы проиграли. Было слово:", word)


