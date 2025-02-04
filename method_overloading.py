class Demo:
    def add(self, a, b, c=0):
        return a+b+c

d=Demo()
print(d.add(2, 3))
print(d.add(1, 2, 3))