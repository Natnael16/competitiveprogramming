
def reverseParentheses(s):
    l = len(s)
    for i in range(len(s)):
        if s[i] != ")":
            continue
        else:
            save = ''
            end = i
            for j in range(i-1,-1,-1):
                if s[j] == "(":
                    if len(s) == l:
                        s = s.replace(s[j:end+1]," "+save+" ")
                        print(s[j:end+1])
                        break
                else:
                    save += s[j]
            print(save,'yess')
        out = ""
        for i in s:
            if i != " ":
                out += i
    return out
print(reverseParentheses("(i(love)you)"))
print(reverseParentheses("(helloworld)"))