# polymorphism
    #overloading - same method name with different arguments
    # PYTHON doesnot support  method overloading.It execute only last method
    #overriding - child class method overrides parent class method


# class Oper:
#     def num(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(self.n1+self.n2)
# class Display:
#     def num(self,n3):
#         self.n3=n3
#         print(self.n3)
# o=Oper()
# o.num(2,3)
# d=Display()
# d.num(3)

# class Oper:
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(self.n1+self.n2)



# class Display:
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(self.n1+self.n2)
#     def __init__(self,n3):
#         self.n3=n3
#         print(self.n3)
# d=Display(2,3)
# d1=Display(2)


# overriding **************************************************************

# class Person:
#     def printval(self,name):
#         self.name=name
#         print(self.name)
# class Child(Person):
#     def printval(self,name):
#         self.name=name
#         print("inside child",self.name)
# d=Child()
# d.printval("abc")

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def printval(self):
#         print(self.name, self.age)
# class Student(Person):
#     def __init__(self,name,age,mark):
#         super().__init__(name,age)
#         # self.name=name
#         # self.age=age
#         self.mark=mark
#
#     def print(self):
#
#         print(self.name)
#         print(self.mark)
# d=Student("chinnu",24,70)
# d.printval()
# d.print()



# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def printval(self):
#         print(self.name, self.age)
# class Employee(Person):
#     def __init__(self,name,age,mark):
#         super().__init__(name,age)
#         # self.name=name
#         # self.age=age
#         self.mark=mark
#
#     def print(self):
#
#         print(self.name)
#         print(self.mark)
# emp=Employee("vinu",24,70)
# emp.printval()
# emp.print()


# class Vehicle:
#     def __init__(self,model,color,regno):
#         self.model=model
#         self.color=color
#         self.regno=regno
#     def printval(self):
#         print(self.color,self.model,self.regno)
#
#     def __str__(self):                             # two string (accepts only string value)
#         return self.model+self.color+str(self.regno)
# v=Vehicle("AZUZ","black",2001)
# v1=Vehicle("amaze","white",1552)
# v.printval()
# print(v1)


# class College:
#     clg="abc college"
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#     def print(self):
#         print(self.name,self.roll,College.clg)
#     def __str__(self):
#         return str(self.roll)+self.name
# ob=College("ammu",12)
# ob1=College("jay",18)
# ob.print()
# print(ob1)

#
# class Employee:
#     company="wipro"
#     def __init__(self,name,exp):
#         self.name=name
#         self.exp=exp
#         print("NAME: ",self.name,"\nEXPERIENCE: ",self.exp,"\nCOMPANY: ",Employee.company)
#     def __str__(self):
#         return self.name+str(self.exp)
# e=Employee("Ammu",2)
# em=Employee("Sanju",3)
# print(em)



