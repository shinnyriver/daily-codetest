from itertools import combinations

N = int(input())

decreasing_numbers = []

for length in range(1, 11):
    for comb in combinations(range(10), length):
        # 내림차순으로 정렬하여 숫자 생성
        num = int(''.join(map(str, sorted(comb, reverse=True))))    #튜플 조작 (4,5) -> 54
        decreasing_numbers.append(num)

decreasing_numbers.sort()

if N < len(decreasing_numbers):
    print(decreasing_numbers[N])
else:
    print(-1)