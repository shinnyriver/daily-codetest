#B3

N = int(input())
numbers = input()
li = []
tmp_li = numbers.split(" ")
for i in range(N):
    li.append(int(tmp_li[i]))
    
li.sort()
answer = str(li[0]) + " " + str(li[-1])
print(answer)