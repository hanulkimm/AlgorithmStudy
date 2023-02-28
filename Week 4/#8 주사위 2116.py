import sys
sys.stdin = open('input.txt', 'r')

dct = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

def find_mx(idx1, idx2, i): # 위, 아래를 제외한 주사위 면 중 최대값
    full = [0, 1, 2, 3, 4, 5]
    full.remove(idx1)
    full.remove(idx2)
    mx = 0
    for j in full:
        if mx < arr[i][j]:
            mx = arr[i][j]
    return mx

def repeat(top): 
    global ans
    idx = -1
    for i in range(1, n): # 주사위 2번부터
         for j in range(6): # 주사위 숫자들
             if arr[i][j]==top:
                 idx = j
         top = arr[i][dct[idx]]
         ans += find_mx(idx, dct[idx],i)


n = int(input())
arr = []
for i in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)


real = 0
for i in range(6): 
    ans = 0 # 합
    top = arr[0][i] # 첫번째 주사위의 숫자들을 하나하나씩 top으로 돌려보기
    ans += find_mx(i, dct[i], 0)
    repeat(top)
    if real < ans:
        real = ans
print(real)