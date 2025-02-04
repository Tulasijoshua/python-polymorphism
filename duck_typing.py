class Duck:
    def swim(self):
        print("I am a duck and I can swim")
    def speaks(self):
        print("Quack Quack")

class Dog:
    def swim(self):
        print("I am a dog and I can swim")
    def speaks(self):
        print("woof woof")

class Person:
    def speaks(self):
        print("blah blah blah")

class Demo:
    def display(self, obj):
        obj.swim()
        obj.speaks()
        print("Information displayed")
d=Duck()
dog = Dog()
p=Person()
demo = Demo()
demo.display(dog)
demo.display(d)
# demo.display(p)