a,b = map(int, input().split())

original_a, original_b = a, b
while b:
    a, b = b, a % b
g = a

l = (original_a * original_b) // g

print(g)
print(l)
