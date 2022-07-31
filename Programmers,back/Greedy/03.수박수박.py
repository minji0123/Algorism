# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

def solution(n):
    수 = '수'
    박 = '박'
    answer = [0]*(n)
    for i in range(n):
        if i % 2 == 0:
            answer[i]= 수
        else:
            answer[i] = 박

    return ''.join(answer)


def solution2(n):
    수 = '수'
    박 = '박'
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer = answer + 수
        else:
            answer = answer + 박

    return answer



def solution3(n):
    return ('수박' * n )[:n]

def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)

def solution(n):
    return "".join(["수박"[i%2] for i in range(n)])


print(solution(3))
print(solution2(3))
