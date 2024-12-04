# validate years from 1800-2024
from re import fullmatch
pattern="((18|10)[0-9]){2}|20[01][0-9]|202[0-4])"
year=input("enter year")
matcher=fullmatch(pattern,year)
if matcher==None:
    print("invalid")
else:
    print("valid")