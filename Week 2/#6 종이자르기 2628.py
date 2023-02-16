import sys
sys.stdin = open('input.txt','r')

width, height = map(int, input().split()) # 가로 세로 길이
n = int(input())

# [1] 가로, 세로로 자르는 경우를 리스트로
lst_garo = []
lst_sero = []
for _ in range(n):
    dr, num = map(int, input().split())
    if dr == 0: #가로로 자르는 경우
        lst_garo.append(num)
    else: # 세로로 자르는 경우
        lst_sero.append(num)

# print(lst_garo , lst_sero)
# [3, 2] [4]


# [2] 오름차순 정렬하기
for i in range(len(lst_garo)-1, 0, -1):
    for j in range(i):
        if lst_garo[j] > lst_garo[j+1]:
            lst_garo[j] , lst_garo[j + 1] = lst_garo[j+1], lst_garo[j]

for i in range(len(lst_sero)-1,0,-1):
    for j in range(i):
        if lst_sero[j] > lst_sero[j+1]:
            lst_sero[j] , lst_sero[j + 1] = lst_sero[j+1], lst_sero[j]
# print(lst_garo , lst_sero)
# [2, 3] [4]

#[3] 잘랐을 때의 부분 길이들 구하기
length_garo = []
length_sero = []
st = 0
for i in lst_garo:
    length_garo.append(i-st) # 2-0=2, 3-2=1
    st = i
length_garo.append(height-st) # 8-3=5

st = 0
for i in lst_sero:
    length_sero.append(i-st)  #4-0=4
    st = i
length_sero.append(width-st) # 10-4=6
# print(length_garo, length_sero)
# [2, 1, 5] [4, 6]

# [4] 가로, 세로 곱한 경우 중 최대 넓이 구하기
ans = 0
for i in length_garo:
    for j in length_sero:
        if ans < i * j:
            ans = i * j
print(ans)



## 메서드 사용 ##
w, h = map(int, input().split())
n = int(input())

lst_garo = []
lst_sero = []
for _ in range(n):
    dr, num = map(int, input().split())
    if dr == 0: #가로로 자르는 경우
        lst_garo.append(num)
    else: # 세로로 자르는 경우
        lst_sero.append(num)

lst_garo.sort()
lst_sero.sort()

lst_garo.append(h)
lst_sero.append(w)
length_garo = []
length_sero = []
st = 0
for i in lst_garo:
    length_garo.append(i-st)
    st = i

st = 0
for i in lst_sero:
    length_sero.append(i-st)  
    st = i
print(length_sero)
ans = max(length_garo) * max(length_sero)
print(ans)