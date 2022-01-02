N, K = map(int, input().split())

coins = []
ans = 0

for _ in range(N):
    coins.append(int(input()))

for i in range(len(coins)-1, -1, -1):
    if K == 0:
        break

    if coins[i] > K:
        continue

    ans += K // coins[i]
    K %= coins[i]

print(ans)