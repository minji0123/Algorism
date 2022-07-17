####################################################
# 전화번호가 문자열 phone_number로 주어졌을 때,
# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution 을 완성

####################################################
# https://school.programmers.co.kr/learn/courses/30/lessons/12948


def solution(phone_number):

    return "*" * (len(phone_number) - 4) + phone_number[-4:]


# print(solution())
print(solution("01033334444"))
print(solution("027778888"))

