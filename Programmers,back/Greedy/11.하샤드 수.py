# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.

# https://school.programmers.co.kr/learn/courses/30/lessons/12947
####################################################

def solution(x):
    numbers = list(map(int, str(x)))

    sum_list = sum(numbers)
    if x % sum_list == 0:
        return True
    else:
        return False



print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
