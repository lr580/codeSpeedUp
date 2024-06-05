n = int(input()) # number of legs
m = int(input()) # number of heads
for x in range(n + 1):
    y = m - x
    if 2 * x + 4 * y == n and x >= 0 and y >= 0:
        print(f'Chicken={x} Rabbit={y}')
        break
else:
    print("No solution!")