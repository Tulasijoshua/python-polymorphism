class ComplexNumber:
    def __init__(self, r, i):
        self.real=r
        self.imaginary=i
    def __add__(self, other):
        # return f"{self.real + other.real} + {self.imaginary+other.imaginary}i"
        return str(self.real+other.real) + "+" + str(self.imaginary+other.imaginary) + "i"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

c1=ComplexNumber(1,2)
c2=ComplexNumber(4,5)
print(c1+c2)

p1 = Person("Daniel", 6)
p2 = Person("Caleb", 14)
if p1 > p2:
    print(f"{p1.name} will pay the bill.")
else:
    print(f"{p2.name} will pay the bill.")
