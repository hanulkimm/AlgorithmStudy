def find_set(x):
    if x == rep[x]:
        return x
    rep[x] = find_set(rep[x])
    return rep[x]

def union(x,y):
    rep[find_set(y)]=find_set(x)

n, m = map(int, input().split())
rep = [i for i in range(n+1)]

for _ in range(m):
    i, a, b = map(int, input().split())
    if i:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
