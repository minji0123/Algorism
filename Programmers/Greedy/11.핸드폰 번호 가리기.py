####################################################
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식
# "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"
####################################################

# 공백은 아무리 밀어도 공백
# s는 알파벳 소문자, 대문자, 공백

def solution(s, n):
    sentense = s
    answer = ""
    대문자 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    소문자 = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(sentense)):
        if sentense[i] in 대문자:
            new_idx = (대문자.find(sentense[i]) + n) % len(대문자)
            answer += 대문자[new_idx]
        elif sentense[i] in 소문자:
            new_idx = (소문자.find(sentense[i]) + n) % len(소문자)
            answer += 소문자[new_idx]
        else:
            answer += sentense[i]

    return answer


# print(solution())
print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
