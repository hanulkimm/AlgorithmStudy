k = int(input())
w = w_idx = h = h_idx = 0
num = []
for i in range(6):
    dr, n = map(int, input().split())
    num.append(n)
    if dr == 1 or dr == 2:
        if w < n:
            w = n
            w_idx = i
    else:
        if h < n:
            h = n
            h_idx = i

large = w * h
s_h = abs(num[(w_idx-1)%6] - num[(w_idx+1)%6]) # 양옆
s_w = abs(num[(h_idx-1)%6] - num[(h_idx+1)%6])
small = s_h*s_w
ans = large - small
print(ans*k)