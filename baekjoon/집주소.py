# import sys
# sys.stdin = open('집주소.txt')


while True:
    arr = [input()]
    # 1*(숫자길이 + 1) == 여백
    # 2*('1'의 개수), 4*('0'의 개수), 3*(나머지의 개수)
    if len(arr) == 1:
        break
    else:
        cnt = 0
        for i in range(len(arr)):
            cnt += len(arr)+1
            if arr[i] == '1':
                cnt += 2
            elif arr[i] == '0':
                cnt += 4
            else:
                cnt += 3
        print(cnt)

