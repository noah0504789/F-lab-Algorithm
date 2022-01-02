def solution(sizes):

    width = max(map(max, sizes))
    length = max(map(min, sizes))

    return width*length

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))