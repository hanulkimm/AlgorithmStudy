import sys
sys.stdin = open('input.txt', 'r')

# from the back ##
n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)][::-1]

cnt = 0 # 쓸 수 있는 시간
ans = 0
for lst in arr:
    if len(lst) == 1:
        cnt += 1 
    else:
        cnt += 1
        if lst[2] <= cnt: # 시간 내에 풀 수 있다면
            ans += lst[1] # 점수 더해주고
            cnt -= lst[2] # 총 쓸 수 있는 시간에서 쓴 시간 빼주기
        else:
            cnt = 0 # 시간 내에 못 풀면 시간 reset해주기!!! 안해주면 뒤에서 못 풀 문제도 풀림
print(ans)
