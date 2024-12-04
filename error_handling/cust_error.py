def poll(age):
    assert age>18, "invalid age"
    print("voted")
try:
    poll(14)
except Exception as e:
    print(e)

def review(rating):
    assert rating>0,"too low"
    assert rating in range(0,11),"too high"
    print("rated")


def is_leap_year(year):
    if year<0:
        return False
    if year%100!=0 and year%4==0 or year%100==0 and year%400==0:
        return True
    else:
        return False
def test_is_leap_year():
    assert is_leap_year(2024)==True,"non century"
    