s = "hello"
p = "ll"




def kmp(s, p, _next):
    i = 0
    j = 0
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = _next[j]
    if j == len(p): return i - j
    return -1
def getNext(p):
    _next = [0] * len(p)
    _next[0] = -1
    #print(_next)
    i = 0
    j = -1
    while i < len(p) - 1:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            #print(i, j)
            _next[i] = j
        else:
            j = _next[j]
    return _next

print(kmp(s, p, getNext(p)))

