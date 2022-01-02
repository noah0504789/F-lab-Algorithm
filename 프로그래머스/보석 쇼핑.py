gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

def solution(gems):
    if len(set(gems)) == 1:
        return [1, 1]

    answer = []
    shortest = len(gems) + 1

    start_p = 0
    end_p = 1

    check_len = len(set(gems))
    contained = {gems[0]:1, }

    while end_p < len(gems):

        if gems[end_p] not in contained:
            contained[gems[end_p]] = 1
        else:
            contained[gems[end_p]] += 1

        if len(contained) == check_len:
            while start_p < end_p:
                if contained[gems[start_p]] > 1:
                    contained[gems[start_p]] -= 1
                    start_p += 1

                elif shortest > end_p - start_p:
                    shortest = end_p - start_p
                    answer = [start_p + 1, end_p + 1]
                    break

                else:
                    break

        end_p += 1

    return answer

print(solution(gems))
