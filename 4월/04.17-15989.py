N = int(input())

for _ in range(N):
    target = int(input())
    dp = [0]*(target+1)
    dp[0] = 1
    
    for i in range(1, target+1):
        dp[i] += dp[i-1]
    
    for i in range(2, target+1):
        dp[i] += dp[i-2]
    
    for i in range(3, target+1):
        dp[i] += dp[i-3]
    
    print(dp[target])