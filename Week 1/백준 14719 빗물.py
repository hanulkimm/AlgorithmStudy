import sys

sys.stdin = open('input.txt', 'r')

h, w = map(int, input().split())
lst = list(map(int, input().split()))
n = len(lst)

# [1] 행과 열 반대로 생각한 행렬 만들어서 전치행렬 만들기
arr = [[0] * h for _ in range(w)]
for i in range(n):
    num = lst[i]
    for j in range(num):
        arr[i][h - j - 1] = 1 # 뒤에서 부터 1 채워주기

arr2 = list(zip(*arr)) # 이게 사용할 행렬

ans = 0
for lst2 in arr2:
    for i in range(w-2): # 1이 최소 한 개 있을 범위
        if lst2[i] == 1:
            for j in range(i+1,n):
                if lst2[j] == 1:
                    ans += j-i-1 # 1 사이의 0의 개수
                    break
        else:
            continue

print(ans)






