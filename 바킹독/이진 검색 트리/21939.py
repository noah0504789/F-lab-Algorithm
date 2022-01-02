class Question(object):
    def __init__(self, number, difficulty):
        self.number = number
        self.difficulty = difficulty

    def __gt__(self, other):
        if self.difficulty == other.difficulty:
            return self.number > other.number
        return self.difficulty > other.difficulty

    def __lt__(self, other):
        if self.difficulty == other.difficulty:
            return self.number < other.number
        return self.difficulty < other.difficulty

qsList = []

for _ in range(int(input())):
    number, difficulty = map(int, input().split())
    qsList.append(Question(number, difficulty))

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'add':
        qsList.append(Question(int(command[1]), int(command[2])))

    elif command[0] == 'recommend':
        if command[1] == '1':
            print(max(qsList).number)

        elif command[1] == '-1':
            print(min(qsList).number)

    elif command[0] == 'solved':
        for qs in list(filter(lambda x: x.number == int(command[1]), qsList)):
            qsList.remove(qs)

