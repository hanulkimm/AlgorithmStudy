def solution(today, terms, privacies):
    ty, tm,td = map(int, today.split('.'))
    dct = {}
    for term in terms:
        a, b = term.split()
        dct[a]=int(b)
    answer = []

    for i in range(len(privacies)):
        info = privacies[i]
        date, kind = info.split()
        y,m,d = map(int, date.split('.'))
        m += dct[kind]
        if m > 12:
            num_y = m // 12
            m = m - 12*num_y
            y += num_y
            if m == 0: # 12월이면
                y -= 1 # 년도 1 빼주고
                m = 12 # 월은 12월
        d -= 1
        if d == 0: 
            m -= 1
            d = 28

        if y < ty:
            answer.append(i+1)
            continue
        elif y ==ty and m < tm:
            answer.append(i+1)
            continue
        elif y ==ty and m == tm and d < td:
            answer.append(i + 1)
            continue

    return answer

print(solution(	"2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))