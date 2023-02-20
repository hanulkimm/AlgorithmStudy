import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = []
for _ in range(n):
    l, h = map(int, input().split())
    arr.append([l, h])
arr.sort()
print(arr)
ans = 0
i = 0
while i < n:
    for j in range(i+1, n):
        flag = False
        if arr[i][1] <= arr[j][1]:
            ans += (arr[j][0] - arr[i][0]) * arr[i][1]
            flag  = True
            i = j
            break
    if flag == False:
        ans += arr[i][1]
        mx = 0
        for k in range(i+1, n):
            if mx < arr[k][1]:
                mx = arr[k][1]
        ans += mx * (arr[n-1][0]-arr[i][0])
        break
if i == n-1:
    ans += arr[i][1]
print(ans)




# for i in range(n-1,0,-1):
#     for j in range(i):
#         if arr[j][-1] > arr[j+1][-1]:
#             arr[j][-1], arr[j+1][-1] = arr[j+1][-1], arr[j][-1]
# print(arr)
