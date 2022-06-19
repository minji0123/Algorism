# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력하고, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

# K1KA5CB7  -> ABCKK13

# import re
# val = "K1KA5CB7"
#
# numbers = re.sub(r'[^0-9]', '', val)
# alphas = list(filter(str.isalpha, val))
# print(''.join(sorted(alphas)) + ''.join(sorted(numbers)))

# print(alpha)
# print(numbers)
# print(sorted(val))


# input = input()

####################################################

val = input()
alpha_array = []
number = 0

for array in val:
    if array.isalpha():
        alpha_array.append(array)
    else:
        number += int(array)

alpha_array.sort()
if number != 0:
    alpha_array.append(str(number))

print(''.join(alpha_array))
