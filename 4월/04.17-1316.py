N = int(input())

count = 0
for _ in range(N):
    word = input()
    check = {}
    is_group = True
    prev = ''
    
    for w in word:
        if w in check and prev != w:
            is_group = False
            break
        check[w] = True
        prev = w
    
    if is_group:
        count += 1

print(count)                