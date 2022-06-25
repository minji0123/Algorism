
# 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려줌.
# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있다.
# 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌릴 수 있음

####################################################

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
# 체육수업을 들을 수 있는 학생의 최댓값을 return

####################################################

# n	lost	reserve	  return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	        4
# 3	[3]	    [1]	        2
####################################################

# # 학생 수 입력받기
# n = int(input())
# 학생배열 = []
#
# # 체육복 훔침당한 학생 번호
# lost = list(map(int, input().split()))
#
# # 여벌체육복 가져온 학생 번호
# reserve = list(map(int, input().split()))
#
# # lost 인 학생만큼 체육복수 - 을 해줌
# 수업들을학생수 = n - len(lost)
#
# for i in range(n):
#     if
#     # 만약에 reserve 번째면서
#         # 양 옆 중 한명이라도 lost 번째면은 수업들을학생수 +1을 해준다
#         # 아니면 말고
#
# print(학생배열)
#
# # 체육복 수가 0이 아닌 애들을 count 해주는거임


# def solution(n, lost, reserve):
#     answer = 0
#
#     return answer


def solution(n, lost, reserve):
    # reserve 에 있는 요소를 하나씩 돌면서
    lost.sort()
    reserve.sort()
    sub_reserve = reserve.copy()
    lost = list(set(lost) - set(reserve))
    lost = list(set(lost) - set(reserve))

    for r in reserve:
        for l in lost:
            if l == r-1:
                lost.remove(l)
                break  # 하나 찾으면 바로 끝내기
            elif l == r+1:
                lost.remove(l)
                break # 하나 찾으면 바로 끝내기

    return n - len(lost)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(1, [1], [1]))
print(solution(5, [1,2,3], [2,3,4]))
print(solution(5, [1,2,3,4], [2,3,4,5]))

print(solution(2, [1, 2], [1, 2]))