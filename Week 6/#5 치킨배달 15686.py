import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations

def distance(i,j): # 모든 치킨집까지 거리 구하기
    lst = []
    for ni,nj in chick_lst:
        lst.append(abs(i-ni)+abs(j-nj))
    return lst

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chick_lst = [] # 치킨집의 좌료
chick_num = 0 # 치킨집의 개수
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            chick_lst.append((i,j))
            chick_num += 1
total = [] # 각 집에서 치킨집까지의 거리 모음
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            total.append(distance(i,j)) # 치킨집까지 거리 구하기

numb = list(range(chick_num)) # 치킨집 번호(그냥 행,열 빠른 순)

ans = 2500
for pick in combinations(numb,m): # 순열 조합구하기
    tmp_a = 0
    for lst in total:
        tmp = [] # 폐업아닌 치킨집까지 거리 모음
        for i in pick:
            tmp.append(lst[i])
        tmp_a += min(tmp) # 최소 거리 더하기
    if ans > tmp_a: # 도시의 치킨 거리가 최소일 때
        ans = tmp_a
print(ans)

