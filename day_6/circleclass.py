class circle:
    pi=3.14159
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.pi *self.r*self.r
    def circum(self):
        return 2*circle.pi*self.r
c=circle(7.5)
print('area=',c.area())
print('circumference=',c.circum())
