N = int(input())

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def make_prime(num, length):
    if length == N:
        print(num)
        return
    
    for i in range(1, 10, 2):
        next_num = num * 10 + i
        if check_prime(next_num):
            make_prime(next_num, length + 1)

# 첫 자리는 2,3,5,7만 가능
for idx in [2,3,5,7]:
    make_prime(idx, 1)