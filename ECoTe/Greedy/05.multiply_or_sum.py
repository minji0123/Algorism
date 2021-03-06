# S: 각 자리가 숫자로만 이루어진 문자열 (0~9)
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 x + 연산자를 넣어 만들어질 수 있는 가장 큰 수를 구하는 프로그램
# 연산은 왼쪽부터 순서대로 이루어진다. (x 가 + 보다 먼자 연산되지 않음)
# 02984 => 576
# 567 -> 210

####################################################
# 대부분 x 가 값을 더 크게 만들지만, 0 1 이면 + 가 값을 더 크게 만든다.
# 두 수가 모두 2 이상인 경우에만 x 를 한다.

####################################################

# s 입력받고 첫 번째 문자(왼쪽 숫자) 저장
s = input()
left_s = int(s[0])

# 맨 처음 문자를 뺀 범위만큼 배열 만들어서 for 문 생성
for i in range(1, len(s)):

    # 두번재 문자(오른쪽 숫자) 저장
    right_s = int(s[i])
    # 두 수 가 하나라도 0,1 인 경우 더하기 수행
    if right_s <= 1 or left_s <= 1:
        left_s += right_s
    else:
        left_s *= right_s

print(left_s)

