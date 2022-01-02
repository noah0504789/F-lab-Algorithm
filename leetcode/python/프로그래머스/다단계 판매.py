# enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# seller = ["young", "john", "tod", "emily", "mary"]
# amount = [12, 4, 2, 5, 10]

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]

def solution(enroll, referral, seller, amount):
    from collections import defaultdict
    import math

    amount = list(map(lambda x: x*100, amount))
    tree = defaultdict(str)
    answer = defaultdict(int)

    def compensate(seller, mine, bonus):
        nonlocal amount, answer, tree

        answer[seller] += mine - bonus

        if tree[seller] == "-" or bonus < 1:
            return

        compensate(tree[seller], bonus, math.floor(bonus * 0.1))

    for i in range(len(enroll)):
        tree[enroll[i]] = referral[i]
        answer[enroll[i]] = 0

    for idx, sel in enumerate(seller):
        compensate(sel, amount[idx], math.floor(amount[idx] * 0.1))

    return list(answer.values())

print(solution(enroll, referral, seller, amount))