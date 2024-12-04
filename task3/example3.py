def roman_to_integer(s):
    roman_values={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
    total=0
    prev_value=0
    for char in reversed(s):
        current_value=roman_values[char]
        if current_value<prev_value:
            total -=current_value
        else:
            total +=current_value
            prev_value=current_value
    return total
s = "MCMXCIV"
print(roman_to_integer(s))

def is_subsequence(s, t):
    i, j= 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
    s1 = "abc"
    t1 = "ahbgdc"
    print(is_subsequence(s1, t1))