N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j][k]: (i,j) 위치에 파이프가 k 방향으로 놓여있을 때의 경우의 수
# k = 0: 가로, 1: 세로, 2: 대각선
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

# 초기값 설정 - (0,1)에 가로방향으로 놓여있는 상태
dp[0][1][0] = 1

for i in range(N):
    for j in range(1, N):  # 첫 번째 열은 제외
        if i == 0 and j == 1:  # 초기 상태는 건너뛰기
            continue
            
        if graph[i][j] == 0:  # 현재 위치가 벽이 아닐 때
            # 가로 방향으로 올 수 있는 경우
            if j-1 >= 0:
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
                
            # 세로 방향으로 올 수 있는 경우
            if i-1 >= 0:
                dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
                
            # 대각선 방향으로 올 수 있는 경우
            if i-1 >= 0 and j-1 >= 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

# 마지막 위치(N-1, N-1)에서 모든 방향의 경우의 수 합
answer = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2]
print(answer)