def is_palindrome(lst):
    return lst == lst[::-1]
lst=[1,2,3,2,1]
if is_palindrome(lst):
   print("The list is a palindrome")
else:
    print("The list is not a palindrome")
