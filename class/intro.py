# object oriented programming
    # class :design pattern/ blueprint
    # object : real world entity
    # reference : to perform operations on object

# class Person:
#     def walk(self):                               # self denotes the method is inside the class
#         print("person is walking")
#     def read(self):
#         print("person is reading")
# obj1= Person()
# obj1.walk()
# obj1.read()
#
# obj2= Person()
# obj2.walk()
# obj2.read()


class Person:

    def setval(self,name,age):
        self.name=name                # instance variable
        self.age=age

    def printval(self):
        print("name :",self.name)
        print("age :",self.age)

obj1= Person()
obj1.setval('Anu',23)
obj1.printval()