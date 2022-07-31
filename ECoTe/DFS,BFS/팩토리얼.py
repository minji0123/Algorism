def 반복팩토리얼(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


def 재귀팩토리얼(n):
    if n <= 1:
        return 1
    return n * 재귀팩토리얼(n-1)

a = int(input())
print(재귀팩토리얼(a))

# print('반복->',반복팩토리얼(5))
# print('반복->',재귀팩토리얼(5))
