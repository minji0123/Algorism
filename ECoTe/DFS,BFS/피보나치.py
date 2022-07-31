memo = [0] * 50
def 피(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n]:
        return memo[n]

    memo[n] = 피(n - 1) + 피(n - 2)
    return memo[n]

def 피(n):
    if n == 0:
        return 0
    elif n == 1:
        return 110
    return 피(n - 1) + 피(n - 2)

def 피(n):
    memo = [0, 1]
    for i in range(2,n+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n]

a = int(input())
print(피(a))