ans = 0

def isPrime(num):
    import math

    if num == 1:
        return False

    l = int(math.sqrt(num)) + 1

    for n in range(2, l):
        if num % n == 0:
            return False
    return True

candidates = [0] * int(input())
candidates = list(map(int, input().split()))

for num in candidates:
    if isPrime(num):
        ans+=1

print(ans)