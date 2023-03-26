def solution(rows, columns, queries):
    answer = []
    arr = []
    for i in range(rows):
        tmp = []
        for j in range(1, columns + 1):
            tmp.append(j + columns * i)
        arr.append(tmp)

    def rotate(si, sj, ei, ej):
        tmp1 = arr[si][ej]
        for cj in range(ej, sj, -1):
            arr[si][cj] = arr[si][cj - 1]

        tmp2 = arr[ei][ej]
        for ci in range(ei, si + 1, -1):
            arr[ci][ej] = arr[ci - 1][ej]
        arr[si + 1][ej] = tmp1

        tmp3 = arr[ei][sj]
        for cj in range(sj, ej - 1):
            arr[ei][cj] = arr[ei][cj + 1]
        arr[ei][ej - 1] = tmp2

        for ci in range(si, ei - 1):
            arr[ci][sj] = arr[ci + 1][sj]
        arr[ei - 1][sj] = tmp3

    def min(si, sj, ei, ej):
        mn = 10000
        for nj in range(sj, ej + 1):
            if mn > arr[si][nj]:
                mn = arr[si][nj]
            if mn > arr[ei][nj]:
                mn = arr[ei][nj]
        for ni in range(si, ei + 1):
            if mn > arr[ni][sj]:
                mn = arr[ni][sj]
            if mn > arr[ni][ej]:
                mn = arr[ni][ej]
        answer.append(mn)

    for query in queries:
        si, sj, ei, ej = query
        si, sj, ei, ej=si - 1, sj - 1, ei - 1, ej - 1
        rotate(si, sj, ei, ej)
        min(si, sj, ei, ej)

    return answer

print(solution(6,6,[[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))