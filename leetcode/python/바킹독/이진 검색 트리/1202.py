import heapq

n, k = map(int, input().split())
gem = []

for _ in range(n):
    w, v = map(int, input().split())
    heapq.heappush(gem, [w, v])

bag = []

for _ in range(k):
    capacity = int(input())
    heapq.heappush(bag, capacity)

res = 0
capable_gem = []

for _ in range(k):
    capacity = heapq.heappop(bag)

    while gem and capacity >= gem[0][0]:
        [w, v] = heapq.heappop(gem)
        heapq.heappush(capable_gem, -v)

    if capable_gem:
        res -= heapq.heappop(capable_gem)
    elif not gem:
        break

print(res)