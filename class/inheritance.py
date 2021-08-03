
# over loading and overriding doesnot support ( shows error )





# 1. single inheritance ************************************************

# class Person:                                          # parent class/ super class/ base class
#     def pdetails(self,name,age,adrs):
#         self.name=name
#         self.age=age
#         self.adrs=adrs
#         print(self.name,self.age,self.adrs)
# class Student(Person):                                # child class / derived class / sub class
#     def sdetails(self,rollno,dpt,mark):
#         self.rollno=rollno
#         self.dpt=dpt
#         self.mark=mark
#         print(self.rollno,self.dpt,self.mark)
#         print(self.name," mark is ",self.mark)
# pe=Person()
# pe.pdetails("Vinu",12,"xyz home")
# st=Student()
# st.pdetails("anu",23,"abc home")
# st.sdetails(100,"commerce",85)


# class Person:
#     def pdetails(self,name,age,adrs):
#         self.name=name
#         self.age=age
#         self.adrs=adrs
#         print(self.name,self.age,self.adrs)
# class Employee(Person):
#     def sdetails(self,id,dpt,salary):
#         self.id=id
#         self.dpt=dpt
#         self.salary=salary
#         print(self.id,self.dpt,self.salary)
#         print(self.name," salary is ",self.salary)
# pe=Person()
# pe.pdetails("Vinu",12,"xyz home")
# st=Employee()
# st.pdetails("anu",23,"abc home")
# st.sdetails(100,"commerce",85)

# 2. multiple inheritance ***************************************

# class Person:
#     def pvalue(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Child:
#     def cvalue(self,adrs,cls):
#         self.adrs = adrs
#         self.cls=cls
#         print(self.adrs,self.cls)
# class Student(Person,Child):
#     def svalue(self,rollno,mark):
#         self.rollno=rollno
#         self.mark=mark
#         print(self.rollno,self.mark)
# st=Student()
# st.pvalue(" megha",25)
# st.cvalue(" abc ",9)
# st.svalue(2,30)


# class Person:
#     def pvalue(self,name,age):
#         self.name=name
#         self.age=age
#         print("person name=",self.name,"age=",self.age)
# class Parent:
#     def pavalue(self,pname,ads):
#         self.pname=pname
#         self.ads=ads
#         print("parent name=", self.pname, "address=", self.ads)
#
# class Employee(Person,Parent):
#     def evalue(self,id,dpt,salary):
#         self.id=id
#         self.dpt=dpt
#         self.salary=salary
#         print(self.id,self.dpt,self.salary)
#         print(self.name," salary is ",self.salary)
# e=Employee()
# e.pvalue("anju",23)
# e.pavalue("sajitha"," abc home")
# e.evalue(101,"commerce",5000)


# multilevel inheritance ***********************************************

# class Person:
#     def pvalue(self,name,age):
#         self.name=name
#         self.age=age
#         print("person name=",self.name,"age=",self.age)
# class Child(Person):
#     def cvalue(self,adrs,cls):
#         self.adrs = adrs
#         self.cls=cls
#         print(self.adrs,self.cls)
#
# class Student(Child):
#     def svalue(self,rollno,mark):
#         self.rollno=rollno
#         self.mark=mark
#         print(self.rollno,self.mark)
#
# st=Student()
# st.svalue(4,70)
# st.cvalue("abc",9)
# st.pvalue(" amal",25)

# class Person:
#     def pvalue(self,pname,page):
#         self.pname=pname
#         self.page=page
#         print("person name=",self.pname,"\tage=",self.page)
# class Child(Person):
#     def cvalue(self, cname, cage):
#         self.cname = cname
#         self.cage = cage
#         print("child name=", self.cname, "\tage=", self.cage)
#
# class Parent(Person):
#     def pavalue(self, paname, paage):
#         self.paname = paname
#         self.paage = paage
#         print("parent name=", self.paname, "\tage=", self.paage)
#
# class Student(Child):
#     def svalue(self, sname, sage):
#         self.sname = sname
#         self.sage =sage
#         print("student name=", self.sname, "\t age=", self.sage)
# ob=Student()
# ob1=Parent()
# ob.pvalue("anu",31)
# ob.cvalue("manu",23)
# ob1.pavalue("jeeva",25)
# ob.svalue("hary",21)


# create a child class vehicle that inherits all variables and methods of vehicle class ***********************

# class Vehicle:
#     company="bajaj"
#     def printval(self):
#         print(self.color,self.model)
# class Bus(Vehicle):
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#         Vehicle.printval(self)
#     def display(self):
#         # self.model=model
#         # self.color=color
#         print(self.model,self.color,Vehicle.company)
# b=Bus("amm","black")
# b.display()


# create an animal class using constructor and build a child class dog ****************

class Animal:
    def __init__(self, model, color):
        self.model=model
        self.color=color
    def print(self):
        print(self.model,self.color)
class Dog(Animal):
    def  __init__(self, model, color):
        self.model = model
        self.color = color

    def display(self):
        print(self.model, self.color)
a=Animal("cat","white")
d=Dog("dog","brown")
a.print()
d.display()