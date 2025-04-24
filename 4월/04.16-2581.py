def is_prime(N):
    if N < 2:
        return False
    if N == 2:
        return True
    if N % 2 == 0:
        return False
    tmp = int(N ** 0.5)
    for i in range(3, tmp + 1, 2):
        if N % i == 0:
            return False
    return True

M = int(input())
N = int(input())

answer = []

for i in range(M, N + 1):
    if is_prime(i):
        answer.append(i)

if not answer:  # 소수가 없으면 -1 출력
    print(-1)
else:
    print(sum(answer))
    print(answer[0])
