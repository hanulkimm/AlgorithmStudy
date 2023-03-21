from collections import deque

def solution(board):
    n = len(board)
    answer = 1e9
    v = [[0]*n for _ in range(n)]
    directions = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)] # 상하좌우 좌표, 방향 index
    q = deque([(0,0,0,-1)]) # 시작좌표, cost, 방향

    while q:
        i,j,cost,dir_idx = q.popleft()
        if (i,j)==(n-1,n-1) and answer>cost:
            answer = cost
        for direction in directions:
            ni,nj = i+direction[0], j+direction[1]
            if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 0:
                if dir_idx==-1 or dir_idx==direction[2]:
                    add_cost = 100
                else:
                    add_cost = 600
                newcost = cost+add_cost
                if v[ni][nj]==0 or v[ni][nj]+500>newcost:
                    q.append((ni,nj,newcost,direction[2]))
                    v[ni][nj]=newcost
    return answer