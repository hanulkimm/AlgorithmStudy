
# 1. 회의 시간이 빨리 끝나는 순서대로 (예제 정렬대로)
# 2. 회의 시간이 빨리 시작하는 순서대로
# 3. 회의 시작 시간이 끝나는 시간 보다는 커야 됨

## sort 안 쓰고 (but 시간초과) ##
n = int(input())
arr = [list(map(int, input().split())) for  _ in range(n)]
print(arr)

# [1] 회의 끝나는 시간 기준으로 오름차순 정리
for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[j][1] > arr[j+1][1]:
            arr[j][1] , arr[j + 1][1] = arr[j + 1][1], arr[j][1]

# [2] 동일한 끝나는 시간의 경우, 시작 시간 기준으로
for i in range(n-1):
    if arr[i][1] == arr[i+1][1]:
        if arr[i][0] > arr[i+1][0]:
            arr[i][0] , arr[i + 1][0] = arr[i + 1][0], arr[i][0]
# [3] 가능한 회의 최대 개수 구하기
cnt = 0
endtime= 0
for i in range(n):
    if endtime <= arr[i][0]:
        cnt += 1
        endtime = arr[i][1]
print(cnt)

## sort 쓰고 ##
arr.sort(key=lambda x :x[0]) # [2] 
arr.sort(key = lambda x : x[1]) # [1]