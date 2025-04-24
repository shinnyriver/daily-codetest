from collections import deque

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))

print(len(result))
for num in sorted(result):
    print(num)
