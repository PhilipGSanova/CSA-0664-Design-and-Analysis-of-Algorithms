def matching(s,t):
    for i in range(len(s)-len(t)):
        j,m=0,i
        while(j!=len(t)):
            if s[m]==t[j]:
                j+=1
                m+=1
            else:
                break
        if j == len(t):
            return True
    return False
s="Philip"
t="ild"
print(matching(s,t))