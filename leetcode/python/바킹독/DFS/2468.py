import sys
from collections import deque
import copy
sys.setrecursionlimit(100000)
r = sys.stdin.readline

N = int(r())
array = [list(map(int, r().split())) for _ in range(N)]

DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = 0
visit = set()

ROWS, COLS = len(array), len(array[0])

mn = min(map(min, array))
mx = max(map(max, array))

def bfs(r, c, arr):
    global visit, ROWS, COLS

    queue = deque()

    queue.append((r, c))
    visit.add((r, c))

    while queue:
        cr, cc = queue.popleft()

        for i in range(4):
            nr = cr + DIR[i][0]
            nc = cc + DIR[i][1]

            if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in visit and
                    arr[nr][nc] is True):
                queue.append((nr, nc))
                visit.add((nr, nc))

for i in range(mn, mx):
    tmp = copy.deepcopy(array)
    res = []
    for j in tmp:
        res.append(list(map(lambda x: x > i, j)))

    ans = 0

    for p in range(ROWS):
        for q in range(COLS):
            if res[p][q] is True and (p, q) not in visit:
                bfs(p, q, res)
                ans += 1

    answer = max(answer, ans)
    visit = set()

print(answer)
