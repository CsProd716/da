class NegRadiusError(Exception):
    pass
#class CharRadiusError(Exception):
    #pass
class circle:
    def __init__(self,radius):
        if (radius)<0:
            raise NegRadiusError
        
        else:
            self.radius = radius
    def area(self):
        return (self.radius**2)*3.14
try:
    r = float(input("Give in a radius"))
    c = circle(r)
    print(c.area())
except NegRadiusError:
    print("Negative radius not allowed")
#except CharRadiusError:
   # print("characters not allowed")
