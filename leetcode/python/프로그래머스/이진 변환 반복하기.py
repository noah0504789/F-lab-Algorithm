def solution(s):
    cnt = 0
    zero = 0

    while True:
        if s == '1':
            break
        zero += s.count("0")
        s = s.replace("0", "")

        s = bin(len(s))[2:]
        cnt += 1

    return [cnt, zero]

print(solution("110010101001"))