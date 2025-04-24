target = 100
N = 9

heights = [int(input()) for _ in range(N)]

found = False
for i in range(N):
    for j in range(i + 1, N):
        if sum(heights) - heights[i] - heights[j] == target:
            real_heights = [h for k, h in enumerate(heights) if k != i and k != j]
            found = True
            break
    if found:
        break

real_heights.sort()
for height in real_heights:
    print(height)