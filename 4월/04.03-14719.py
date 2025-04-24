#G5

y, x = map(int, input().split())

y_list = list(map(int, input().split()))

height = max(y_list)

prefix = [0]
check = 0
max_sum = 0
for i in range(1, x+1):
    prefix.append(max(prefix[i-1],y_list[i-1]))
    if prefix[i] == height:
        check = i
        break
if check == x:
    for i in range(len(prefix)):
        max_sum += prefix[i]

else:
    suffix = [0] * x
    suffix[-1] = y_list[x-1]    #index5 = 2

    for i in range(x-1 , check, -1):
        suffix[i - 1] = (max(suffix[i], y_list[i-1]))

    for i in range(len(prefix)):
        if prefix[i] != 0:
            max_sum += prefix[i]

    for j in range(len(suffix)):
        if suffix[j] != 0:
            max_sum += suffix[j]
sum_y = 0
for i in y_list:
    sum_y += i
answer = max_sum - sum_y

print(answer)