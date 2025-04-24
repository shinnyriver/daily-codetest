from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*(M) for _ in range(N)]

def bfs(y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
    
    return visited[N-1][M-1]

print(bfs(0, 0))