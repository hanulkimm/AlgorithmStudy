import sys
sys.stdin = open('input.txt', 'r')

V = int(input())
n = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(n):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

v =[0]*(V+1) # 방문 표시
stk = [] # 돌아갈 곳 표시
s = 1
v[s] = 1
alst = [] # 지나간 곳 표시(stack이랑 구분)

while True:
    for e in adj[s]:
        if v[e] == 0: # 미방문 시
            stk.append(s)
            s = e
            v[s] = 1
            alst.append(s)
            break
    else:
        if stk:
            s = stk.pop()
        else:
            break

print(len(set(alst))) # 중복 제거

