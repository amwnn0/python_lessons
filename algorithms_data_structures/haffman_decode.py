k, l = [int(i) for i in input().split()]
dct = {}
for _ in range(k):
    value, key = input().split(": ")
    dct[key] = value
string = input()
i = 0
result = []
while string:
    i += 1
    if string[:i] in dct:
        result.append(dct[string[:i]])
        string = string[i:]
        i = 0
print("".join(result))
