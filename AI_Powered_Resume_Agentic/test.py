s = input()

xvowels = "aeiout"
result = []
i = 0

while i < len(s):
    start = i

while i < len(s) and s[i] not in xvowels:
    i += 1

length = i - start

if length >= 2:
    for j in range(start, i):
        result.append(s[j].upper())
    else:
        result.append(s[start])

else:
    result.append(s[start])
    i += 1

print("".join(result))