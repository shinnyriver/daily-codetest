from collections import deque

N, M, K = map(int, input().split())
graph = [['X'] * (M+1) for _ in range(N+1)]
visited = [[False] * (M+1) for _ in range(N+1)]

for _ in range(K):
    y,x = map(int, input().split())
    graph[y][x] = 'O'

def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    size = 1
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while q:
        cy, cx = q.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if 1 <= ny <= N and 1 <= nx <= M:
                if not visited[ny][nx] and graph[ny][nx] == 'O':
                    visited[ny][nx] = True
                    q.append((ny,nx))
                    size += 1
    
    return size

result = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if not visited[i][j] and graph[i][j] == 'O':
            result = max(result, bfs(i,j))

print(result)