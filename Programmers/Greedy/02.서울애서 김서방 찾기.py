


def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = i

    return "김서방은 "+ str(answer) +"에 있다"


def solution2(seoul):
    return ('김서방은 %d에 있다' %seoul.index('Kim'))


def solution3(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

print(solution(["Jane","Kim"]))
print(solution2(["Jane","Kim"]))
print(solution3(["Jane","Kim"]))