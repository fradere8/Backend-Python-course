n = int(input())
digits = 1
count_before = 0
while digits * 9 * 10 ** (digits - 1) <= n:
    count_before += digits * 9 * 10 ** (digits - 1)
    digits += 1

start_num = 10 ** (digits - 1) + (n - count_before - 1) // digits

position = (n - count_before - 1) % digits
print(int(str(start_num)[position]))