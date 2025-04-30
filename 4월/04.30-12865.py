import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i번째 물건까지 고려했을 때, j 무게에서의 최대 가치
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i-1]
    for j in range(1, K + 1):
        if j >= weight:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])