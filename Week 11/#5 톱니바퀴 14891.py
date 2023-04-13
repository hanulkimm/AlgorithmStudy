def clock(i,dir):
    if dir ==1:
        save = arr[i][7]
        for j in range(7,0,-1):
            arr[i][j]=arr[i][j-1]
        arr[i][0] = save
    else:
        save = arr[i][0]
        for j in range(8):
            if j==7:
                arr[i][j]=save
            else:
                arr[i][j]=arr[i][j+1]

def opposite(a,b):
    if arr[a][2] != arr[b][6]:
        return True
    else:
        return False


arr = [list(map(int, input())) for _ in range(4)]
dct = {1:-1, -1:1}
k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    num -= 1

    if num==0:
        if opposite(num,num+1):
            if opposite(num+1,num+2):
                if opposite(num+2,num+3):
                    clock(num+3,dct[dir])
                clock(num+2,dir)
            clock(num+1,dct[dir])

        clock(num, dir)

    elif num==1:
        if opposite(num-1,num):
            clock(num-1,dct[dir])
        if opposite(num,num+1):
            if opposite(num+1,num+2):
                clock(num + 2, dir)
            clock(num + 1, dct[dir])
        clock(num, dir)
    elif num==2:
        if opposite(num,num+1):
            clock(num+1,dct[dir])
        if opposite(num-1,num):
            if opposite(num-2,num-1):
                clock(num -2, dir)
            clock(num -1, dct[dir])
        clock(num, dir)
    else:
        if opposite(num-1, num):
            if opposite(num -2, num-1):
                if opposite(num -3, num-2):
                    clock(num -3, dct[dir])
                clock(num - 2, dir)
            clock(num - 1, dct[dir])

        clock(num, dir)

ans = 0
for i in range(4):
    if arr[i][0]:
        ans += 2**i
print(ans)