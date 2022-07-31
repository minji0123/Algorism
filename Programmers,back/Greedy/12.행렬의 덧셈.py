####################################################
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과
####################################################
# https://school.programmers.co.kr/learn/courses/30/lessons/12950

#
def solution(arr1, arr2):
    # arr3 = [[] * len(arr1)]
    # arr3 = [[] for _ in range(len(arr1)) ]
    arr3 = []
    for i in range(len(arr1)):
        arr3.append([])

    print(len(arr1))
    print(arr3)
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            a = arr1[i][j] + arr2[i][j]
            arr3[i].append(a)
    return arr3


# def solution(arr1, arr2):
#     배열 = [[0] * len(arr1[0])] * len(arr1)
#     print(배열)
#     for i in range(len(arr1)):
#         for j in range(len(arr1[0])):
#             배열[i][j] = arr1[i][j] + arr2[i][j]
#             print(배열)
#     return 배열


print(solution([[1, 2, 9, 8, 9, 9, 89], [2, 3, 9, 8, 9, 9, 89]], [[3, 4, 9, 8, 9, 9, 89], [5, 6, 9, 8, 9, 9, 89]]))
print(solution([[1, 2, 3], [3, 4, 5],  [3, 4, 5]], [[1, 2, 3], [3, 4, 5], [3, 4, 5]]))
print(solution([[1], [2]], [[3], [4]]))
# print(solution([[], []], [[], []]))
