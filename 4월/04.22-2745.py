B, N = input().split()
N = int(N)
cnt = len(B)
answer = 0

for letter in B:
    if letter.isdigit():
        num = int(letter)
    else:
        num = ord(letter) - ord('A') + 10
    answer += num * (int(N) ** (cnt-1))
    cnt -= 1

print(answer)