class MarksNotEligible(Exception):
    pass
class NotValidInt(Exception):
    pass
try:
    l = []
    for i in range(3):
        t = int(input("Enter marks"))
        l.append(t)
        if t<20 and t>=0:
            raise MarksNotEligible
        if t<0:
            raise NotValidInt
except MarksNotEligible:
    print("Marks are not eligible")
except NotValidInt:
    print("The input is not valid")
