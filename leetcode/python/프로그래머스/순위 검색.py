from bisect import bisect_left

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    slist = [[] for _ in range(4*3*3*3)]
    infoDir = {'cpp':1, 'java':2, 'python':3, '-':0,
               'backend':1, 'frontend':2,
               'junior':1, 'senior':2,
               'chicken':1, 'pizza':2
    }

    for i in info:
        language, position, career, food, score = i.split()
        # info에 따른 각 자리의 값을 미리 구해둠
        arr = (infoDir[language] * 3 * 3 * 3,
                infoDir[position] * 3 * 3,
                infoDir[career] * 3,
                infoDir[food])

        # info를 하이픈값으로 구성하여 하이픈 query에 대해 정보를 리턴받을 수 있도록 경우의 수를 구한 후 인덱스에 score 더하기
        for i in range(1<<4): # 0000 ~ 1111 (16가지 경우의 수)
            idx = 0
            for j in range(4): # 0000, 0010, 0100, 1000
                if i & (1 << j): # j값과 i값의 자리 비트수가 같은 경우
                    idx += arr[j]
            slist[idx].append(int(score))

    for i in range(4 * 3 * 3 * 3):
        slist[i] = sorted(slist[i]) # 해당 조건에 대해서 X점 이상 받은 사람의 수를 구하기 위해 정렬하기

    for string in query:
        w = string.split()
        # and가 query에 들어있음.
        idx = infoDir[w[0]*3*3*3 + infoDir[w[2]]*3*3 + infoDir[w[4]]*3 + wmap[w[6]]]
        score = int(w[7])
        answer.append(len(slist[idx]) - bisect_left(slist[idx], score))

    return answer




print(solution(info, query))