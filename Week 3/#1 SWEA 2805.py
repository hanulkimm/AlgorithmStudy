## 농작물 수확하기 ##
# 각 행 마다 수확하는 열의 길이를 기준으로
# 열의 개수가 아니라 시작점과 끝나는 점을 기준으로 접근
# 1행에서 중간행까지 수확하는 열의 시작점과 끝점이 1씩 멀어짐
# 중간행에서 끝행 까지는 1씩 가까워짐


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    m = (n-1)//2
    ans = 0
    sj, ej = m, m # 1행에서 수확할 때 열의 시작, 끝점
    for i in range(n): # 각 행마다 돌면서
        for j in range(sj, ej+1): 
            ans += arr[i][j]
        if i < m: # 중간행 전까지( 열의 길이가 커진다)
            sj -= 1
            ej += 1
        else: # 수확하는 열의 길이가 작아진다
            sj += 1
            ej -= 1
    print(f'#{tc} {ans}')