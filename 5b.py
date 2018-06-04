class triangle:
    def __init__(self,ang1,ang2,ang3):
        self.number_of_sides = 3
        self.ang1 = ang1
        self.ang2 = ang2
        self.ang3 = ang3
    def check_angles(self):
        if (self.ang1+self.ang2+self.ang3) == 180:
            return True
        else:
            return False

a = float(input("Give in the first angle"))
b = float(input("Give in the second angle"))
c = float(input("Give in the third angle"))
my_triangle = triangle(a,b,c)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())
