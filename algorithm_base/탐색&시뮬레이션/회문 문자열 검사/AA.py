# import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
for i in range(1, n+1):
    word = input().upper()
    res = ''
    for j in range(len(word)//2):
        if word[j] == word[len(word)-1-j]:
            continue
        else:
            res = "NO"
            break
    else:
        res = "YES"
    print('#{} {}'.format(i, res))