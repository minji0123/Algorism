
####################################################
# 단어 s의 가운데 글자를 반환하는 함수
# 단어의 길이가 짝수라면 가운데 두글자를 반환
####################################################

# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    길이 = len(s)

    if 길이 %2 ==0:
        return s[길이//2-1]+s[길이//2]

    elif 길이 %2 ==1:
        return s[길이//2]


print(solution("abcde"))
print(solution("qwer"))
