def 유(큰수, 작은수):
    if 큰수 % 작은수 == 0:
        return 작은수
    else:
        return 유(작은수, 큰수 % 작은수)


print(유(192,162))
