import sys
sys.stdin = open('input.txt')

#지나간 경로 저장 함수
def dfs(s, V):
    visited = [0]*(V+1)
    stack = [] #1,2,4,6,5,7,3 경로 저장
    i = s #현재 방문한 접점 i
    visited[i] = 1 #현재 시작점 == True(1)
    #node[i] = 1  i는 1
    print(node[i])
    while i != 0: #True
        for w in range(1, V+1):
            #인접하고               아직 방문 x
            if adj[i][w] == 1 and visited[w] == 0 :
                stack.append(i) #방문경로저장
                i = w
                visited[w] = 1 #현 정점 업데이트
                print(node[i])
                break #방문 1회 했으니 break
        #for문 다 끝나고
        else:
            #stack에 값이 있으면
            if stack:
                i = stack.pop()
            else:
                i = 0 #break i가 0이면 while문 끝남
V = 7 #접점 갯수 1~7
E = 8 #엣지 갯수
connect = list(map(int, input().split()))
#점
connect_pt = []
for i in range(0, len(connect), 2):
    #1,2    1,3   2,4  이렇게 점 좌표들을 넣는다
    sub = [connect[i], connect[i+1]]
    connect_pt.append(sub)

# print(connect_pt)
#connect_pt의 좌표들에 1을 넣어라

adj = [[0]*(V+1) for _ in range(V+1)] #행,열이 0~7까지

#connect_pt에 해당하는 값들마다 바꿔줄거니까
for i in range(len(connect_pt)):
    x = connect_pt[i][0]  # connect_pt에서의 각 리스트 x좌표
    y = connect_pt[i][1]  # connect_pt에서의 각 리스트 y좌표
    adj[x][y] = 1
    adj[y][x] = 1
# print(adj)

node = ['',1,2,3,4,5,6,7]
#1은 시작점, 7은 숫자의 개수다
dfs(1,7)

#함수 내에 프린트가 있는 경우 함수 호출만 해줘도 결과가 나온다
#함수 내에 프린트가 있는 경우, 프린트로 함수를 다시 불러오면 결과와 함께 마지막에
#None을 반환한다

#이를 방지하기 위해, 함수 내에 프린트 대신, return을 써준다.!~!~!~!!~
#이 경우에는 무조건 함수를 프린트로 불러와야한다. 오~!!!넹! ㅎㅎ

#위의 두가지 방법은 틀린 것이 아니라, 다른 것이다!!!!