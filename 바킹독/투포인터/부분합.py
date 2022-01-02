n, s = map(int, input().split())
lst = list(map(int, input().split()))
ans = int(2e9)

l, r = 0, 0
SUM = 0
while True:
    if SUM >= s:
        ans = min(ans, r-l)
        SUM -= lst[l]
        l += 1
    elif r == n:
        break
    else:
        SUM += lst[r]
        r += 1

if ans == int(2e9):
    print(0)
else:
    print(ans)