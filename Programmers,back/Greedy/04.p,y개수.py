
# https://programmers.co.kr/learn/courses/30/lessons/12916

#  s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return
def solution(s):
    s_list = list(s)
    p,y = 0, 0
    for i in range(len(s_list)):
        if s_list[i] == 'p' or s_list[i] == 'P':
            p = p+1
        elif s_list[i] == 'y' or s_list[i] == 'Y':
            y = y+1
    return p == y

# def solution(s):
#     if (s.upper().count('P') == s.upper().count('Y')):
#         return True
#     return False
#
#     return p == y

print(solution("pPoooyY"))
