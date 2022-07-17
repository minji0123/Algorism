
####################################################
# 각 단어는 하나 이상의 공백문자로 구분
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴
####################################################
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
# https://programmers.co.kr/learn/courses/30/lessons/12930
# 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.

def solution(s):
    arr = []
    word_index = 0
    for i in range(len(s)):
        if s[i] == ' ':
            word_index = 0
            arr.append(s[i])
        elif word_index % 2 == 0:
            word_index += 1
            arr.append(s[i].upper())
        elif word_index % 2 == 1:
            word_index += 1
            arr.append(s[i].lower())

    return ''.join(arr)

print(solution(" try hello world"))




