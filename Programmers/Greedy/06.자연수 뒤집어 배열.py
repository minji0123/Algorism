# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴

# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    num_list = list(map(int, str(n)))
    return num_list.reverse()

print(solution(12345))
