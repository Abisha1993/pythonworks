from re import finditer
f=open("C:\\Users\\jebin\\OneDrive\\Desktop\\pythonworks\\processing_json\\regularexpressinons\\social_post.txt")

for line in f:
    words=line.rstrip("\n")
    pattern="#\w+"
    matcher=finditer(pattern,words)
    for obj in matcher:
        print(obj.group())