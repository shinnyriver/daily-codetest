N = int(input())
li = []
for _ in range(N):
    li.append(list(input()))

def check_row():
    max_cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if li[i][j] == li[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt

def check_col():
    max_cnt = 1
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if li[i][j] == li[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt

max_candy = 1

# 가로로 인접한 사탕 교환
for i in range(N):
    for j in range(N-1):
        li[i][j], li[i][j+1] = li[i][j+1], li[i][j]
        max_candy = max(max_candy, check_row(), check_col())
        li[i][j], li[i][j+1] = li[i][j+1], li[i][j]

# 세로로 인접한 사탕 교환
for i in range(N-1):
    for j in range(N):
        li[i][j], li[i+1][j] = li[i+1][j], li[i][j]
        max_candy = max(max_candy, check_row(), check_col())
        li[i][j], li[i+1][j] = li[i+1][j], li[i][j]

print(max_candy)

