# 8 8 좌표평면
# 나이트는 L 자 형태로만 이동할 수 있고, 정원 밖으로 나갈 수 없다.
#   수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
#   수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
# 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램 작성
#   세로: 12345678
#   가로: abcdefgh
# a1    2

####################################################
# 리스트를 이용해서 8가지 방향에 대한 벡터를 정의한다.

시작위치 = input()
현_세로 = int(시작위치[1])
현_가로 = int(ord(시작위치[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
count = 0

for step in steps:
    세로이동 = 현_세로 + step[0]
    가로이동 = 현_가로 + step[1]
    if 세로이동 >= 1 and 세로이동 <= 8 and 가로이동 >= 1 and 가로이동 <= 8:
        count += 1

print(count)
