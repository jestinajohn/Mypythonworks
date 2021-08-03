# constructor :  to initialise instance variable
# constructor automatically invokes when object is created


# class Person:
#
#     def __init__(self,name,age,address):
#         self.name=name                # instance variable
#         self.age=age
#         self.address=address
#     def printval(self):
#         print("name :",self.name)
#         print("age :",self.age)
#         print("address :",self.address)
#
# obj1= Person('Anu',23,"abc home")
# obj2= Person('Sunu',28,"abc home")
# obj1.printval()
# obj2.printval()


# class Calculator:
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#     def add(self,n1,n2):
#         print(n1+n2)
#
#     def mult(self,n1,n2):
#         print(n1*n2)
#
#     def sub(self,n1,n2):
#         print(n1-n2)
#
#     def div(self,n1,n2):
#         print(n1/n2)
#
# n1 = float(input("enter first number"))
# n2 = float(input("enter second number"))
# ob=Calculator(n1,n2)
# ob.add(n1,n2)
# ob.mult(n1,n2)
# ob.sub(n1,n2)
# ob.div(n1,n2)

class Teacher:
    clg="abc college"
    def __init__(self,id,name,sub,dept):
        self.id=id
        self.name=name
        self.sub=sub
        self.dept=dept

    def printval(self):
        print("id : ",self.id)
        print("name :",self.name)
        print("subject :",self.sub)
        print("department :",self.dept)
        print("college :",Teacher.clg)

obj1= Teacher(101,'Anu',"maths","commerce ")

obj2= Teacher(102,'kunu',"english","home science")
obj1.printval()
print("\n")
obj2.printval()