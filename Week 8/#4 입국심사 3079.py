import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
s, e = min(arr) , max(arr)*m # 최소 시간, 최대 시간
ans = e
while s<=e:
    total = 0 # 심사 가능한 전체 사람 수
    mid = (s+e)//2

    for i in range(n):
        total += mid//arr[i] # 한 심사대에서 심사할 수 있는 사람

    if total >= m: # 충분히 심사 할 수 있다면(시간이 충분함)
        e = mid - 1
        if ans > mid:
            ans = mid
    else:
        s = mid +1
print(ans)