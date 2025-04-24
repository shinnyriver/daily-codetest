string = list(input().strip())
tmp = string.copy()

inverse_string = []
while tmp:
    inverse_string.append(tmp.pop())

print(1 if inverse_string == string else 0)