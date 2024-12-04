def merge_strings():
    word1="abc"
    word2="pqr"
    merged=[]
    i,j=0,0
    while i<len(word1) and j<len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i +=1
        j +=1
    merged.extend(word1[i:])
    merged.extend(word2[j:])
    return ''.join(merged)
print("merged string:",merge_strings())
