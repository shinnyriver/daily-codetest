N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

dp = [10001] * (K+1)  # 최대값으로 초기화 (K는 10000이하)
dp[0] = 0  # 0원을 만드는데 필요한 동전 개수는 0개

for coin in coins:
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])
