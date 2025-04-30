import sys
from collections import deque
input = sys.stdin.readline 

N = int(input())
K = int(input())
answer = []

graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(K):
    start, end = map(int, input().split())
    graph[start][end] = True
    graph[end][start] = True

def bfs():
    visited = [False] * (N+1)
    visited[1] = True
    queue = deque()
    queue.append(1)
    
    while queue:
        current = queue.pop()
        for i in range(1, N+1):
            if graph[current][i] and not visited[i]:
                visited[i] = True
                answer.append(i)
                queue.append(i)
    
    return len(answer)

print(bfs()) 