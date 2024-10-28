# class Demo:
#     # def add(self, a, b, c=0):
#     #     return a+b+c
#     def add(self, *args):
#         total=0
#         for i in args:
#             total=total+i
#         return total
# d=Demo()
# print(d.add(2, 3))
# print(d.add(1,2,3))
# print(d.add(1,2,3,4,5,6))

class Father:
    def sleep(self):
        print("sleeps from 10:00 PM to 5:00 AM")
    def eat(self):
        print("eating")

class Son(Father):
    def sleep(self):
        print("sleeps from 2:00 AM to 5:00 AM")
        super().sleep()

son_1 = Son()
son_1.sleep()