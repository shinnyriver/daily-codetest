idx = 1
cnt = 0
N = int(input())

while(True):
    if N - idx >= 0:
        N -= idx
        cnt += 1
        idx += 1
    else:
        break

print(cnt)
