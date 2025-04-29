from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

q = deque()
for _ in range(N):
    commands = list(input().split())
    if commands[0] == "push":
        q.append(int(commands[1]))
    elif commands[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif commands[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
    elif commands[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif commands[0] == "size":
        print(len(q))
    elif commands[0] == "empty":
        print(0 if q else 1)
 