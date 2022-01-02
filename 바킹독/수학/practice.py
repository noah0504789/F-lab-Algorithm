def isPrime(num):
    import math
    if num == 1:
        return False

    l = int(math.sqrt(num))

    for n in range(2, l+1):
        if num % n == 0:
            return False
    return True

def sieve(num):
    if num == 1:
        return False

    nums = [True for _ in range(num+1)]
    primes = []

    for n in range(2, num+1):
        if not nums[n]:
            continue

        for m in range(n*2, num+1, n):
            nums[m] = False

    for i in range(2, num+1):
        if nums[i]:
            primes.append(i)

    return primes

def prime_factorization(num):
    import math
    l = int(math.sqrt(num)) + 1

    for i in range(2, l):
        while num % i == 0:
            num /= i
            print(i)

    if num != 1:
        print(int(num))

def divisor(num):
    import math

    l = int(math.sqrt(num)) + 1
    div = []

    for i in range(2, l):
        if num % i == 0:
            div.append(i)

    for j in range(len(div)-1, -1, -1):
        if (div[j] * div[j]) == num: continue
        div.append(int(num / div[j]))

    print(div)


# print(isPrime(6))
# print(sieve(36))
# prime_factorization(9991)
divisor(18)