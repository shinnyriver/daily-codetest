def calculate(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        if a < 0:
            return -((-a) // b)
        return a // b

def backtrack(idx, result):
    global max_val, min_val
    
    if idx == N:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            backtrack(idx + 1, calculate(result, numbers[idx], i))
            operators[i] += 1

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_val = float('-inf')
min_val = float('inf')

backtrack(1, numbers[0])

print(max_val)
print(min_val)
