import sys
input = sys.stdin.readline

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)
max_value = 0

for i in range(N-1, -1, -1):    # N-1부터 0까지 -1
    time = li[i][0] + i     # li[i][0] == i일에 걸리는 시간,
    if time <= N:
        dp[i] = max(li[i][1] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)