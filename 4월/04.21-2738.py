N, M = map(int, input().split())

matrix_1 = [list(map(int, input().split())) for _ in range(N)]
matrix_2 = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * M for _ in range(N)]
for m in range(M):
    for n in range(N):
        answer[n][m] = matrix_1[n][m] + matrix_2[n][m]


for n in range(N):
    print(*answer[n])