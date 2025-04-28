from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

coins = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def is_out(y, x):
    return y < 0 or y >= N or x < 0 or x >= M

def bfs():
    q = deque()
    y1, x1 = coins[0]
    y2, x2 = coins[1]
    q.append((y1, x1, y2, x2, 0))
    visited = set()
    visited.add((y1, x1, y2, x2))
    
    while q:
        y1, x1, y2, x2, cnt = q.popleft()
        if cnt >= 10:
            return -1
        for d in range(4):
            ny1, nx1 = y1 + dy[d], x1 + dx[d]
            ny2, nx2 = y2 + dy[d], x2 + dx[d]
            
            out1 = is_out(ny1, nx1)
            out2 = is_out(ny2, nx2)
            
            if out1 and out2:
                continue
            elif out1 or out2:
                return cnt + 1
            
            # 벽이면 이동하지 않음
            if not out1 and board[ny1][nx1] == '#':
                ny1, nx1 = y1, x1
            if not out2 and board[ny2][nx2] == '#':
                ny2, nx2 = y2, x2
            
            if (ny1, nx1, ny2, nx2) not in visited:
                visited.add((ny1, nx1, ny2, nx2))
                q.append((ny1, nx1, ny2, nx2, cnt + 1))
    return -1

print(bfs())
