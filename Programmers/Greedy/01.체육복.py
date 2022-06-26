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


# solution 1

def solution(n, lost, reserve):
    # 받은 배열값 정렬
    lost.sort()
    reserve.sort()
    # remove() 시 배열값이 줄어드는 현상을 방지하기 위한 copy
    sub_reserve = reserve.copy()
    # 여벌 체육복을 가져온 학생이 체육복을 도둑맞았을 경우의 처리
    for r in sub_reserve:
        for l in lost:
            # 자기 자신이 체육복을 도둑맞았을 때의 경우 remove
            if l == r:
                lost.remove(l)
                reserve.remove(l)
                break

    # 체육복 빌려주기 로직 시작
    for r in reserve:
        for l in lost:
            # 체육복 번호 기준 왼쪽 사람에게 우선 빌려주기
            if l == r - 1:
                lost.remove(l)
                break
            elif l == r + 1:
                lost.remove(l)
                break
    # 체육수업 들을 학생 return
    return n - len(lost)


# solution2
def solution2(n, lost, reserve):
    # set() 사용 시 교집합이 맞지 않는 현상을 방지하기 위한 copy
    sub_reserve, sub_lost = reserve.copy(), lost.copy()
    # set() 사용으로 여벌 체육복을 가져온 학생이 체육복을 도둑맞았을 경우 처리 (교집합 제거)
    lost, reserve = sorted(list(set(sub_lost) - set(sub_reserve))), sorted(list(set(sub_reserve) - set(sub_lost)))

    # 체육복 빌려주기 로직 시작
    for r in reserve:
        # 체육복 번호 기준 왼쪽 사람에게 우선 빌려주기 (if in 써도됨)
        if lost.count(r - 1):
            lost.remove(r - 1)
            continue
        elif lost.count(r + 1):
            lost.remove(r + 1)
            continue
    # 체육수업 들을 학생 return
    return n - len(lost)

# print(solution(5, [2, 4], [1, 3, 5]))
# print(solution(5, [2, 4], [3]))
# print(solution(3, [3], [1]))
# print(solution(1, [1], [1]))
# print(solution(5, [1,2,3], [2,3,4]))
# print(solution(5, [1,2,3,4], [2,3,4,5]))
#
# print(solution(2, [1, 2], [1, 2]))


# if r in lost:
#
#
# for l in lost:
#     if r == l :