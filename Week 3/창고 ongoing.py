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
    if arr[i][1] < arr[i+1][1]:
        ans += (arr[i+1][0]+1 - arr[i][0]) * (arr[i+1][1]-arr[i][1])



