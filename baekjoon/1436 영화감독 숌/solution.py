import sys
sys.stdin = open('input.txt')

N = int(input())

cnt = 0

number = 0
while cnt != N:
    if '666' in str(number):
        cnt += 1
    if cnt == N:
        break
    number += 1
print(number)