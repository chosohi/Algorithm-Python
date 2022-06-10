'''
반복문을 이용한 문제풀이
1) 1부터 N까지 홀수출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수출력하기
'''

n = int(input())
# 2
# res = 0
# for i in range(1, n+1) :
#     if i%2 == 1 :
#         res += i
# print(res)

# 3
for i in range(1, n+1) :
    if n%i==0:
        # 줄바꿈 안함
        print(i, end=" ")     