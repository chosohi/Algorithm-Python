N, M, V = map(int, input().split())

v = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]

for _ in range(M):
  a,b = map(int, input().split())
  v[a].append(b)
  v[b].append(a)

for i in v:
  i.sort()

print(v)

answer = []

# cur : 현재 위치 (current) 즉 현재 어떤 노드 번호인지 나타냄
# 한 번 방문한 곳은 다시 안가겠다.
def DFS(cur):
  
  for i in v[cur]:
    if visited[i]:
      continue
    visited[i] =True
    answer.append(i)
    DFS(i)
    
# 시작 노드는 DFS 안에서 처리 안해주기 때문에 그에 대한 처리를 한다.
visited[V] = True
answer.append(V)
DFS(V)
print(*answer)