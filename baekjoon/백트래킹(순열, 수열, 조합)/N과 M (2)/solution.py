import sys
sys.stdin = open('baekjoon/백트래킹(순열, 수열, 조합)/N과 M (2)/input.txt', 'r') #file open

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이다

tc = int(input())


for _ in range(tc) :
    N, M = list(map(int,input().split()))
    visited = [False for i in range(M+10)]
    arr = []
    
    def recur(cur):
        if len(arr) == M:
            print(" ".join(map(str,arr)))
            return
        for i in range(cur,N+1):
            if visited[i]:
                continue
            visited[i] = True
            arr.append(i)
            recur(i+1)
            arr.pop()
            visited[i] = False

    recur(1)
    