# 누적합 이용하기

def solution(board, skill):
    answer = 0
    arr = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        arr[r1][c1] += degree
        arr[r2+1][c1] -= degree
        arr[r1][c2+1] -= degree
        arr[r2+1][c2+1] += degree

    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            arr[i][j+1] += arr[i][j]
    for j in range(len(arr[0])-1):
        for i in range(len(arr) - 1):
            arr[i+1][j] += arr[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + arr[i][j] > 0:
                answer += 1
    return answer

# print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]),10)