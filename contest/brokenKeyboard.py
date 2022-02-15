y = input()


def brokenKeyboard(s):
    di = {}
    res = ''
    if len(s) == 1:
        return 
    for i in s:
        di[i] = di.get(i
        , 0) + 1
    for i in range(1,len(s)-1):
        if di[s[i]] % 2 != 0 or s[i] != s[i + 1] and s[i] != s[i - 1]:
            if s[i] not in res:
                res+= s[i]
    res = sorted(res)
    return "".join(res)


print(brokenKeyboard(y))
