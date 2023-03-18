import sys
sys.stdin = open('input.txt', 'r')

# pypy3 제출..python은 시간초과
def stdev(tmp):
    mean = sum(tmp) / len(tmp)
    var = 0
    for num in tmp:
        var += (num - mean) ** 2
    var = var / len(tmp)
    sd = math.sqrt(var)
    return sd

import math
n, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = 1e9
for i in range(n - K + 1):
    tmp = []
    for j in range(K):
        tmp.append(lst[i + j])
    sd = stdev(tmp)
    if ans > sd:
        ans = sd
    for k in range(i+j+1, n):
        tmp.append(lst[k])
        sd = stdev(tmp)
        if ans > sd:
            ans = sd
print(ans)

## 외부 모듈 쓰면 런타임 에러 
# import numpy as np
# n, k = map(int, input().split())
# lst = list(map(int, input().split()))
# ans = 1
# for i in range(n - k + 1):
#     tmp = []
#     for j in range(k):
#         tmp.append(lst[i + j])
#     stdev = np.std(tmp)
#     if ans > stdev:
#         ans = stdev
# print(ans)