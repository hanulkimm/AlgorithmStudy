from collections import deque

n = int(input())
lst = [i for i in range(1,n+1)]
deq = deque(lst)

while len(deq)>1:
    deq.popleft()
    deq.append(deq.popleft())
print(*deq)