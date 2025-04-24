N = int(input())
li = []
answer = []
for _ in range(N):
    li.append(int(input()))
    
for num in li:
    positions = []
    pos = 0
    while num > 0:
        if num % 2 == 1:
            positions.append(pos)
        num //= 2
        pos += 1
    print(*positions)
    
     