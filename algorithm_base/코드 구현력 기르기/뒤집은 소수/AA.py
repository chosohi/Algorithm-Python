
def reverse(x):
    num = 0
    i = 1
    while len(str(x))-i >= 0:
        if len(str(x))-i < 0 :
            break
        base = 10 ** (len(str(x))-i)
        num += int(str(x)[-i]) * base
        i += 1

    return num
def isPrime(x):
    num = reverse(x)
    for i in range(2, num):
        if num % i == 0:
            break
            return
    else:
        return num
x = isPrime(32)
n = int(input())
res = []
arr = list(map(int, input().split()))
for i in range(n):
    result = isPrime(arr[i])
    if result:
        res.append(result)
print(*res)