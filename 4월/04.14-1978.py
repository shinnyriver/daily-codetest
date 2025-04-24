N = int(input())
li = list(map(int, input().split()))

answer = 0

for num in li:
    if num == 1:
        answer -= 1
        pass
    tmp = int(num ** 0.5)
    answer += 1
    for i in range(2, tmp+1):
        if num % i == 0:
            answer -= 1
            break
        
print(answer)