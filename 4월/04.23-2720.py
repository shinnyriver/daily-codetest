TC = int(input())

for _ in range(TC):
    C = int(input())
    Q, D, N, P = 0,0,0,0
    Q = C // 25
    C %= 25
    D = C // 10
    C %= 10
    N = C // 5
    P = C % 5
    print(Q, D, N, P)