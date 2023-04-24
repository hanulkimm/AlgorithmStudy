from collections import deque
def count(i,j):
    q = deque()
    q.append((i,j))
    arr[i][j]=0
    cnt = 1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]==1:
                arr[ni][nj]=0
                cnt+=1
                q.append((ni,nj))
    ans.append(cnt)
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            count(i,j)
ans.sort()
print(len(ans))
for num in ans:
    print(num)