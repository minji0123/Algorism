# 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다.
####################################################
# https://programmers.co.kr/learn/courses/30/lessons/12943
# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# 작업을 500번 반복할 때까지 1이 되지 않는다면 –1
####################################################

# 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
def solution(num):
    count = 0

    while num != 1:
        if num % 2 == 0:
            num = num / 2
            count +=1
        elif num % 2 ==1:
            num = num * 3 + 1
            count +=1
        if count >500:
            return -1

    return count


print(solution(6))
print(solution(16))
print(solution(626331))
