import heapq 

N,M = map(int,input().split(' '))

edges = [[] for i in range(N)]

deg = [0] * N

for i in range(M):
    x,y = map(int,input().split(' '))
    edges[x-1].append(y-1)
    deg[y-1] += 1

q = []
for i in range(N):
    if deg[i] == 0:
        q.append(i)

ans = []

while q:
    cur = heapq.heappop(q)
    ans.append(cur+1)
    for tmp in edges[cur]:
        deg[tmp] -= 1
        if deg[tmp] == 0:
            heapq.heappush(q,tmp)


if len(ans) == N:
    print(*ans)
else:
    print(-1)