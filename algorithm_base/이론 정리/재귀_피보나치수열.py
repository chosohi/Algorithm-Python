# 재귀에서는 문제 정의와 종료조건이 굉장히 중요하다
# 피보나치 수열이란 : 어떤 수열의 항이, 앞의 두항의 합과 같은 수열
# f(1) = 1
# f(2) = 1
# f(3) = 2
# f(4) = 3
# f(5) = 5
# f(6) = 8
# ...
# f(n-2)+f(n-1) = f(n)

def fibo(n):
    a = 1
    b = 1
    if n == 1 or n == 2:
        return 1
    for i in range(1, n):
        a, b = b, b + a

    return a


print(fibo(5))

