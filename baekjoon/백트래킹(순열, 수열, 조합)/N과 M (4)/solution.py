import sys
sys.stdin = open('baekjoon/백트래킹(순열, 수열, 조합)/N과 M (4)/input.txt', 'r') #file open

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어한다.

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    arr = []

    def recur() :
        if len(arr) == M:
            print(" ".join(map(str, arr)))
            return
        for i in range(1,N+1) :
            if len(arr) and i < arr[-1] :
                continue
            arr.append(i)
            recur()
            arr.pop()
              
    recur()