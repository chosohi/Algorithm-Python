N, M, V = map(int, input().split())

v = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)
    
for i in v:
    i.sort()

answer = []

def DFS(cur) :
    for i in v[cur]:
        if visited[i]:
            continue
        visited[i]=True
        answer.append(i)
        DFS(i)

visited[V] = True
answer.append(V)

DFS(V)

print(*answer)

