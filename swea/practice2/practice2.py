import sys
sys.stdin = open('input.txt')

def Checking(arr):
    stack = []

    top = -1

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append('(')
            top += 1
        else:
            # 여기서 막힌다 유유
            if len(stack) == 0:
                return -1

            else:
                stack.pop()
                top -= 1

    if len(stack):
        return -1
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    result = Checking(arr)

    print('#{} {}'.format(tc, result))
