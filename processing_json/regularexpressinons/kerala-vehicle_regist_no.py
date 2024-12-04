# starting with kl
#2 digit
#alphabets minimum1 maximum2
#4 digit
from re import fullmatch

from re import fullmatch
reg_no=input("enter registration number:")
pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"
matcher=fullmatch(pattern,reg_no)
if matcher==None:
    print("invalid")
else:
    print("valid")
