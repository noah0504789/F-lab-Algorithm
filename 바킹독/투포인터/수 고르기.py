n, m = map(int, input().split())
lst = []
l, r = 0, 0
short = int(2e9)

for i in range(n):
    lst.append(int(input()))

lst.sort()

while r < n:
    if lst[r] - lst[l] < m:
        r += 1
    else:
        short = min(short, lst[r] - lst[l])
        if short == m:
            break
        l += 1

print(short)