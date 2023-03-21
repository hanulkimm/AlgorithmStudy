from collections import deque
def solution(board):
    n = len(board)
    directions = ((-1,0),(1,0),(0,-1),(0,1)) # 상하좌우

    def bfs(x,y,cost,d):
        v = [[0]*n for _ in range(n)] # 방문 표시 대신 최소비용 표시
        q = deque()
        q.append((x,y,cost,d))

        while q:
            x, y, cost, dr = q.popleft()
            for i in range(4):
                ni, nj = x + directions[i][0], y + directions[i][1]

                if 0<=ni<n and 0<=nj<n and board[ni][nj]==0: # 범위내, 벽 아님
                    if dr==i: # 같은 방향
                        newcost = cost + 100
                    else: # 같은 방향 아님, 코너 생김
                        newcost = cost + 600

                    if v[ni][nj]==0 or  v[ni][nj]>newcost: # 첫방문이거나 이미 방문한 경우 보다 값이 작은 경우
                        q.append((ni,nj,newcost,i))
                        v[ni][nj] = newcost # 값 갱신
        return v[n-1][n-1] # 도착점
    return min(bfs(0,0,0,1), bfs(0,0,0,3)) # 아래로 출발, 오른쪽으로 출발 (2가지 경우)