class circle():
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r**2*3.14
    def permiter(self):
        return self.r*2*3.14
a = circle(6)
print(a.area())
print(a.permiter())