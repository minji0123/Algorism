# 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
# 단 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지
# https://programmers.co.kr/learn/courses/30/lessons/12906

####################################################
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
####################################################
#
def solution(arr):
    # arr.append(arr[-1])
    push_arr = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            push_arr.append(arr[i])
    push_arr.append(arr[-1])
    return push_arr


def solution2(arr):
    answer = [arr[0]]
    for x in arr[1:]:
        if answer[-1] != x:
            answer.append(x)
    return answer

def solution3(arr):
    answer = []
    for x in arr:
        if len(answer) == 0 and answer[-1] != x:
            answer.append(x)
    return answer

print(solution([1, 1, 3, 3, 0, 1, 1,1,1,1,1]))
print(solution([4, 4, 4, 3, 3, 3, 2]))
print(solution([4, 4, 4, 4, 4]))
