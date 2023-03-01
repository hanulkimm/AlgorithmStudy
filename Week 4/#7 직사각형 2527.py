## 모든 경우 손으로 그리면서 생각
## 선분 --> 점 순서 (반대로 하면 선분인데 점으로 인식하는 경우가 잘못 분류됨)


for _ in range(4):
    x1,y1,x2,y2,p1,q1,p2,q2 = map(int, input().split())
    # [1] 안 만날 때
    if (x2 < p1) or (p2 < x1) or (y2 < q1) or (q2 < y1):
        ans = 'd'
    # [2] 선분일 때(윗변, 오른쪽변, 아래, 왼쪽)
    elif (y2 == q1 and x1 < p2 and p1 < x2) or (x2 == p1 and q1 < y2 and y1 < q2) or (y1 == q2 and p1 < x2 and x1 < p2) or (x1 == p2 and q1 < y2 and y1 < q2):
        ans = 'b'
    # [3] 점 일때 
    elif (x2, y2)==(p1,q1) or (x2, y1)==(p1,q2) or (x1,y1)==(p2,q2) or (x1,y2)==(p2,q1):
        ans = 'c'
    else:
        ans = 'a'
    print(ans)