import sys
sys.stdin = open('input.txt', 'r')

# 이진탐색
n, M = map(int, input().split())
lst = list(map(int, input().split()))
h = max(lst)
s = 0
e = h
ans = 0
while s <= e:
    m = (s+e)//2
    cnt = 0
    for ch in lst:
        if ch > m:
            cnt += ch - m
    if cnt >= M:
        ans = m
        s = m+1
    elif cnt < M:
        e = m-1

print(ans)
