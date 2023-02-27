# ord('.') = 46
# ord('A') = 65

def preorder(i):
    if i:
        ans1.append(i)
        preorder(left[i])
        preorder(right[i])
def inorder(i):
    if i:
        inorder(left[i])
        ans2.append(i)
        inorder(right[i])
def postorder(i):
    if i:
        postorder(left[i])
        postorder(right[i])
        ans3.append(i)

n = int(input()) # 노드의 개수
left = [0] * (n+1)
right = [0] * (n+1)
for _ in range(n):
    p, l, r = map(ord, input().split())
    p -= 64
    l -= 64
    r -= 64
    if left[p]==0 and l>0:
        left[p] = l
    if right[p]==0 and r>0:
        right[p] = r

ans1 = []
ans2 = []
ans3 = []
preorder(1)
inorder(1)
postorder(1)
for ch in ans1:
    print(chr(ch+64),end='')
print()
for ch in ans2:
    print(chr(ch+64),end='')
print()
for ch in ans3:
    print(chr(ch+64),end='')
