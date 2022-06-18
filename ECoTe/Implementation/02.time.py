# 정수N 이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성
# 5  11475

####################################################

# 시간 = int(input())
# count = 0
# 분초 = 60
# 시간 = 시간 + 1
#
# for hour in range(시간):
#     for min in range(분초):
#         for sec in range(분초):
#             # print( hour," : ", min, " : ",sec)
#             if '3' in str(sec) or '3' in str(min) or '3' in str(hour):
#                 count += 1
#                 # print(count,"개")
#
#
# print("됨?",count)

# if 3 in sec: 이건 안됨

####################################################
# 완전 탐색 문제 유형 (Brute Forcing)

시간 = int(input())
count = 0
분초 = 60
for hour in range(시간+1):
    for min in range(분초):
        for sec in range(분초):
            if '3' in str(sec) + str(min) + str(hour):
                count += 1

# print(sum([sum([sum([1 if '3' in str(sec) + str(min) + str(hour) else 0 for sec in range(분초)]) for min in range(분초)]) for hour in range(시간+1)]))