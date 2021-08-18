import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())+1
    arr = [[0]*n for _ in range(n)]
    # print(arr)
    # 규칙을 찾아랏
    # 이게 5바이5 행렬이라서 첫 행과 열은 다 0이라 1인덱스부터 시작
    for i in range(1, n):
        for k in range(1,i+1):
            if i <= 2:
                arr[i][k] = 1
            else:
                arr[i][k] = arr[i-1][k-1] + arr[i-1][k]
    result = []
    #5바이5에서 4바이4만 탐색한다!
    for i in range(1, n):
        #리스트마다 갱신될 때, result에 넣을 sub
        sub = []
        for j in range(1, n):
            if arr[i][j] != 0:
                #i행에서 0이 아닌 모든값들이 sub에 들어간다
                sub.append(arr[i][j])
        #i가 바뀌기 전에 result에 더한다
        result.append(sub)

    print('#{}'.format(tc))
    for i in result:
        # print(*i)
        # int는 조인함수 없어서 스트링으로 변환해서 출력
        print(' '.join(map(str, i)))
        #진짜 너무 똑ㄸ고하시네....


"""
   1
   1 1
   1 2 1
   1 3 3 1      
      1
     1 1 
    1 2 1
   1 3 3 1

"""

