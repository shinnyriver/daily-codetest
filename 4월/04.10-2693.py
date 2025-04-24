T = int(input())

li = [list(map(int, input().split())) for _ in range(T)]

for l in li:
    l.sort()
    print(l[7])