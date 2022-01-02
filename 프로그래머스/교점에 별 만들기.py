from itertools import combinations as combi

def solution(line):
    n_list = [i for i in range(len(line))]
    start_points = []
    x_list, y_list = [], []

    for i, j in combi(n_list, 2):
        a, b, e = line[i]
        c, d, f = line[j]
        if (a*d - b*c):
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            if x.is_integer() and y.is_integer():
                start_points.append((int(x), int(y)))
                x_list.append(int(x))
                y_list.append(int(y))

    max_x, min_x = max(x_list), min(x_list)
    max_y, min_y = max(y_list), min(y_list)
    x_size = max_x - min_x + 1
    y_size = max_y - min_y + 1

    arr = [['.'] * x_size for _ in range(y_size)]

    for x, y in start_points:
        arr[max_y-y][x-min_x] = '*'

    return [''.join(s) for s in arr]