import sys
sys.stdin = open('baekjoon/백트래킹(순열, 수열, 조합)/N과 M (7)/input.txt', 'r') #file open

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())))
    res = []

    def recur():
        if len(res) == M :
            print(" ".join(map(str, res)))
            return
        
        for i in range(N):
            res.append(arr[i])
            recur()
            res.pop()

    recur()
