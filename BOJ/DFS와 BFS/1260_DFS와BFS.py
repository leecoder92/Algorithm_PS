from collections import deque

def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for w in range(N + 1):
        if adj[v][w] == 1 and not visited[w]:
            dfs(w)

def bfs():
    while q:
        v = q.popleft()[0]
        print(v, end=' ')
        for w in range(N + 1):
            if adj[v][w] == 1 and not visited[w]:
                visited[w] = 1
                q.append([w])

# N: 정점의 개수, M: 간선의 개수, V: 탐색 시작할 정점 번호
N, M, V = map(int, input().split())

# 인접배열 생성
adj = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

visited = [0] * (N + 1)

dfs(V)
print()

visited = [0] * (N + 1)
q = deque()
q.append([V])
visited[V] = 1
bfs()