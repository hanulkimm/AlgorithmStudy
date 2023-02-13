dct = {'(': ')', '[': ']'}
while True:
    st = input()
    if st == '.': # '.'이면 중단
        break
    else:
        ans = 'yes'
        stk = []
        for ch in st:
            if ch == '(' or ch == '[':
                stk.append(dct[ch])
            elif ch == ')' or ch == ']':
                if stk:
                    if stk[-1] == ch:
                        stk.pop()
                    else:
                        ans = 'no'
                else:
                    ans = 'no'
        if stk:
            ans = 'no'
        print(f'{ans}')