import math

n = int(input())
nums = [False for _ in range(n+1)]
lst = []
n2 = int(math.sqrt(n))

for i in range(2, n2+1):
    if nums[i]:
        continue

    for j in range(i*2, n+1, i):
        nums[j] = True

for k in range(2, n+1):
    if not nums[k]:
        lst.append(k)

lng = len(lst)
l, r, SUM = 0, 0, 0
ans = 0

print(lst)

while r < lng:
    SUM = sum(lst[l:r+1])

    if SUM == n:
        ans += 1
        r += 1
        l += 1
    elif SUM > n:
        l += 1
    else:
        r += 1

print(ans)
