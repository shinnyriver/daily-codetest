N = 10
suffix = []
tmp = 0

for _ in range(N):
    to_out, to_in = map(int, input().split())
    tmp += (to_in - to_out)
    suffix.append(tmp)

suffix.sort()
print(suffix[-1])