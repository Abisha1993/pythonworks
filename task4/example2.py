


def is_subsequence(s, t):
    i, j= 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
    s1 = "axc"
    t1 = "ahbgdc"
    print(is_subsequence(s1, t1))