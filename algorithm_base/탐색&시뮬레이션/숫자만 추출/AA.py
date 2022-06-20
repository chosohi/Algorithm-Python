# import sys
# sys.stdin = open("input.txt", "rt")
words = input()
res = ''
for word in words:
    if word in ['0','1','2','3','4','5','6','7','8','9']:
       res += word

res = int(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0 :
        cnt += 1
print(res)
print(cnt)