f=open("C:\\Users\\jebin\\OneDrive\\Desktop\\pythonworks\\datasets\\prog_lang.txt","w")

languages=["python","java","c#","javascript"]

for l in languages:
    f.write(l+"\n")

    f.close()