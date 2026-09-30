text = (input()).lower()
count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

count = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(count[:3])

