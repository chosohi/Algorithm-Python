import sys
sys.stdin = open('input.txt')

# T= int(input())
#
# for tc in range(T):
#

# 65~96
word = input().upper()

res = [0]*97

for val in word:
    res[ord(val)] += 1

if res.count(max(res)) >= 2:
    print("?")
else:
    print(chr(res.index((max(res)))))

