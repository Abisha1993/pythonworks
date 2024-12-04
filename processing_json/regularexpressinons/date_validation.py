#date 01,1,31
from re import fullmatch
date=input("enter date")
pattern=("0[1-9]|[12][0-9]|3[01]")
matcher=fullmatch(pattern,date)
if matcher==None:
    print("invalid")
else:
    print("valid")


# validate years from 1800-2024

from re import fullmatch
pattern=
