N = int(input())
ropes = []
ans = 0

for _ in range(N):
    ropes.append(int(input()))

ropes.reverse()

for i in range(N):
    ropes[i] = ropes[i] * (i+1)

print(max(ropes))