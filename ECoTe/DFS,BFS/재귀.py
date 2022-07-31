def 나1(i):
    if i == 5:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    나1(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')


def 나(i):
    if i == 5:
        return
    # print(i, '번재 내가', i + 1, '번째 나를 부른다.')
    print(i, '번째 집어넣는중 <- ')
    나(i + 1)
    print(i, '번째 빼는중 -> ')

나(1)


# def 재귀함수():
#     print('재귀인거시야')
#     재귀함수()
#
# 재귀함수()

# count = 0
# def 재귀():
#     global count
#     print(count, '번째 재귀인거시야')
#     count += 1
#     재귀()
#
# 재귀()
