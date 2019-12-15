while True:
    a, b, c = map(int, input().split())
    if a < 2100000000 and b < 2100000000 and c < 2100000000:
        break

cnt = 0

while True:
    cnt += 1

    total = a + b * cnt
    profit = c * cnt

    if total < profit:
        break

print(cnt)