a = int(input("first number: "))
b = int(input("second number: "))

r = a % b
# gcd: 81 dan 57
# 81 = 1 (57) + 24
# 57 = 2 (24) + 9
# 24 = 2 (9) + 6
# 9 = 1 (6) + 3
# 3 = 2 (3) + 0

while r:
    a = b
    b = r
    r = a % b

print("GCD adalah:", b)
