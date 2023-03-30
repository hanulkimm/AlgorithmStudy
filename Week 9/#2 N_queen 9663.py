def dfs(i):
    global ans
    if i==n:
        ans += 1
        return
    else:
        for j in range(n):
            if v1[j]==0 and v2[i+j]==0 and v3[i-j]==0:
                v1[j]= v2[i + j] = v3[i - j] = 1
                dfs(i+1)
                v1[j]= v2[i + j] = v3[i - j] = 0

n = int(input())
ans = 0
v1 = [0] * n
v2 = [0] * (2*n-1)
v3 = [0] * (2*n-1)

dfs(0) # 행 번호
print(ans)