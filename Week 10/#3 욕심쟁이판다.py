import sys
sys.stdin = open('input.txt', 'r')

def dfs(i,j,cnt):
    global tmp
    flag = True
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=i+di, j+dj
        if 0<=ni<n and 0<=nj<n and v[ni][nj]==0 and arr[ni][nj]>arr[i][j]:
            flag=False
            v[ni][nj]=1
            dfs(ni,nj,cnt+1)
            v[ni][nj]=0
    if flag:
        tmp = max(tmp, cnt)
        return


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
v = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        tmp = 0
        v[i][j]=1
        dfs(i,  j, 1)
        v[i][j]=0
        ans = max(tmp, ans)
print(ans)
