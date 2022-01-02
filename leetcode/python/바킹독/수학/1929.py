def sieve(start, end):
    import math

    end += 1
    nums = [True] * end

    for n in range(2, int(math.sqrt(end))+1):
        if nums[n]:
            for m in range(2*n, end, n):
                nums[m] = False

    for i in range(start, end):
        if i>1 and nums[i]:
            print(i)

n, m = map(int, input().split())
sieve(n,m)


