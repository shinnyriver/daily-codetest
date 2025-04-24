N, K = map(int, input().split())
tmp = 0

coins = [int(input()) for _ in range(N)]
# dp[i]는 i원을 만들 수 있는 경우의 수
dp = [0] * (K + 1)
dp[0] = 1  # 0원을 만드는 경우는 1가지

# 각 동전에 대해
for coin in coins:
    # 현재 동전으로 만들 수 있는 모든 금액에 대해 경우의 수 계산
    for i in range(coin, K + 1):
        dp[i] += dp[i - coin]

print(dp[K])
