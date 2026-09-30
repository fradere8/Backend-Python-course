n = int(input())
is_prime = [False] * 2 + [True] * (n - 1)
for i in range(2, n):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

for i in range(n):
    if is_prime[i]:
        print(i, end=' ')



