#add two nos using lambda functions

add=lambda n1,n2:n1+n2
print(add(10,20))



#sub two nos using lambda functions

sub=lambda n1,n2:n1-n2

print(sub(10,20))

#find cube using lambda functions

cube=lambda n:n**3

print(cube(3))

#maximum length of two strings

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("hai","morning"))


#smart sub using lambda functions


smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(20,100))


words=["hello","hai","morning","test"]

def get_length(word):
    
    return len(word)
print(max(words,key=get_length))
print(min(words,key=get_length))

#using lambda functions

get_length=lambda word:len(word)
print(max(words,key=get_length))


