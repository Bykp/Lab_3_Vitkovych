p = int(input())

if p == 1:
    print(2)
elif p == 2:
    print(4)
else:
    a, b = 2, 4
    for _ in range(3, p + 1):
        a, b = b, a + b
    print(b)
