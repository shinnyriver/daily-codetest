from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stack = []
output = []

for _ in range(N):
    command = input().split()
    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        if stack:
            output.append(str(stack.pop()))
        else:
            output.append('-1')
    elif command[0] == '3':
        output.append(str(len(stack)))
    elif command[0] == '4':
        output.append('0' if stack else '1')
    elif command[0] == '5':
        if stack:
            output.append(str(stack[-1]))
        else:
            output.append('-1')

print('\n'.join(output))
            