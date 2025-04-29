import sys
input = sys.stdin.readline

N = int(input())
li = [input().strip() for _ in range(N)]

li = list(set(li))
li.sort(key=len, reverse=True)

answer = 0
used = []

for word in li:
    is_prefix = False
    for used_word in used:
        if used_word.startswith(word):
            is_prefix = True
            break
    if not is_prefix:
        used.append(word)
        answer += 1

print(answer)
