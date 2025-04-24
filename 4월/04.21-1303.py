from collections import deque

def bfs(x, y, color):
    queue = deque([(x, y)])
    count = 1
    graph[x][y] = 'X'  # 방문 처리
    
    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 체크 및 같은 색상 확인
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == color:
                queue.append((nx, ny))
                graph[nx][ny] = 'X'  # 방문 처리
                count += 1
    
    return count
N, M = map(int, input().split())

graph = [list(input().strip()) for _ in range(M)]


white = 0
blue = 0

for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            power = bfs(i, j, 'W')
            white += power * power
        elif graph[i][j] == 'B':
            power = bfs(i, j, 'B')
            blue += power * power

print(white, blue)

