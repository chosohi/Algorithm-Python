import sys
sys.stdin = open('baekjoon/백트래킹(순열, 수열, 조합)/N과 M (1)/input.txt', 'r')

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 

T = int(input())

for tc in range(T):
    print("tc",tc)
    N, M = list(map(int,input().split()))


    arr = []
    

    def recur(cur):
        if cur == M:
            
            print(" ".join(map(str, arr)))
            return
        
        
        for i in range(1, N+1):
            if i not in arr:
                arr.append(i)
                recur(cur+1)
                arr.pop()
            
            

    recur(0)
    