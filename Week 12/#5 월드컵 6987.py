import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations
games = list(combinations(range(6), 2)) # 모든 가능한 조별 경기

def dfs(depth):
    global ans
    if depth==15: # 모든 경기 다 고려했을 때
        ans = 1
        for result in results:
            if sum(result)!=0:
                ans =0
                break
        return
    g1, g2 = games[depth]
    for x, y in ((0, 2), (2, 0), (1, 1)):
        if results[g1][x]>0 and results[g2][y]>0:
            results[g1][x] -= 1
            results[g2][y] -= 1
            dfs(depth+1)
            results[g1][x] += 1
            results[g2][y] += 1


for _ in range(4):
    tmp = list(map(int, input().split()))
    results = [tmp[i*3:i*3+3] for i in range(0,6)]
    ans = 0
    dfs(0)
    print(ans, end=' ')