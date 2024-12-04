# validate pancard
# 3alphbet
#4th place alphabet[PCAFHT]
# 1 alphbet
#4 digit
# #1 alphbet

from re import fullmatch
pancard_number=input("enter pancard number")
pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"
matcher=fullmatch(pattern,pancard_number)
if matcher==None:
    print("invalid")
else:
    print("valid")



    #validate_month 01-12
    #date 1 2  3 4 5 6 7 8 9 
          #01 02 03 04 05 06 07 08 09
          #10 11 12
from re import fullmatch
date=input("enter date")
pattern=("[0-9]|0[1-9]|1[0-2]")
matcher=fullmatch(pattern,date)
if matcher==None:
    print("invalid")
else:
    print("valid")

# date 01,1,31

