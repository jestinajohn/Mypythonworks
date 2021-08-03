# class Vehicle:
#     company="Honda"
#     def printval(self):
#         print(self.color,self.model)
# class Car(Vehicle):
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#         Vehicle.printval(self)
#     def display(self):
#         print(self.model,self.color,Vehicle.company)
# b=Car("Amaze","black")
# b.display()



# class College:
#     def cvalue(self,cname,place):
#         self.cname=cname
#         self.place=place
#         print("college name=",self.cname,"\tplace=",self.place)
# class Dept(College):
#     def dvalue(self, dname, id):
#         self.dname = dname
#         self.id = id
#         print("Dept name=", self.dname, "\tId", self.id)
#
# class Parent(College):
#     def pavalue(self, paname, paage):
#         self.paname = paname
#         self.paage = paage
#         print("parent name=", self.paname, "\tage=", self.paage)
#
# class Student(Dept):
#     def svalue(self, sname, sage):
#         self.sname = sname
#         self.sage =sage
#         print("student name=", self.sname, "\t age=", self.sage)
# ob=Student()
# ob1=Parent()
# ob.cvalue("ABC College","TVM")
# ob.dvalue("Commerce",101)
# ob1.pavalue("Madhu",56)
# ob.svalue("Hary",21)





# class Person:
#
#     def __init__(self,name,age,adrs):
#         self.name = name
#         self.age = age
#         self.adrs = adrs
#     def pdetails(self):
#         print(self.name,self.age,self.adrs)
# class Employee:
#     def sdetails(self,id,dpt,salary):
#         self.id=id
#         self.dpt=dpt
#         self.salary=salary
#         print(self.id,self.dpt,self.salary)
# class Demo(Employee):
#     def demo(self,hobby):
#         self.hobby=hobby
#         print("Hobby : ",self.hobby)
# pe=Person("Vinu",12,"xyz home")
# pe.pdetails()
# d=Demo()
# d.sdetails(100,"commerce",85000)
# d.demo("swimming")
#


# class Book:
#
#     def __init__(self,lib,name,author,page):
#         self.lib=lib
#         self.name = name
#         self.author = author
#         self.page = page
#     def bdetails(self):
#         print("Library Name :",self.lib)
#         print("Book Name :", self.name)
#         print("Author :", self.author)
#         print("Pages :", self.page)
# b=Book("college library","Alchemist","Paulo coelo",256)
# b.bdetails()




# class Teacher:
#     def pvalue(self,pname,page):
#         self.pname=pname
#         self.page=page
#         print("Teacher name=",self.pname,"\tage=",self.page)
# class Child(Teacher):
#     def pvalue(self, cname, cage):
#         self.cname = cname
#         self.cage = cage
#         print("child name=", self.cname, "\tage=", self.cage)
# ob=Child()
# ob.pvalue("Anju",26)


# import re
# f1=open('f1','r')
# f2=open('f2','w')
# x = '[+][9][1]\d{10}'
# for i in f1:
#     data = i.rstrip("\n")
#     match = re.fullmatch(x, data)
#     if match is not None:
#         f2.write(i)


# class Student:
#     def __init__(self,name,id,dept,mark):
#         self.name=name
#         self.id=id
#         self.dept=dept
#         self.mark=mark
#     def printdata(self):
#         print(self.name,self.id,self.dept,self.mark)
#
# lst=[]
# file1 = open('sdfile', 'r')
# for i in file1:
#     data=i.rstrip("\n").split(",")
#     print(data)
#     name=data[0]
#     id=data[1]
#     dept=data[2]
#     mark=data[3]
#     s1=Student(name,id,dept,mark)
#     #s1.printdata()
#     lst.append(s1)
# mark = []
# for st in lst:
#     mark.append(st.mark)
# print(mark)
# for st in lst:
#     if (st.mark==max(mark)):
#         print(st.id,st.name,st.dept,st.mark)

# try:
#     s=3//0
#     print(s)
# except:
#     print("exception occurs")
# finally:
#     print("inside finally")



#
# import re
# st=input("enter string")
# x='^[A-Z]\w{3,8}[A-Z]$'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")



# a=lambda num:num%2==0
# print(a(4))


# class Vehicle:
#     def __init__(self,model,color,regno):
#         self.model=model
#         self.color=color
#         self.regno=regno
#     def printval(self):
#         print(self.color,self.model,self.regno)
#
#     def __str__(self):
#         return self.model+self.color+str(self.regno)
# v=Vehicle("AZUZ","black",2001)
# v1=Vehicle("amaze","white",1552)
# v.printval()
# print(v1)




import re
st=input("enter string")
x='^a[0-9]+b$'
match=re.fullmatch(x,st)
if match is not None:
    print("valid")
else:
    print("invalid")


# import re
# st=input("enter string")
# x='[A-Z][a-z]+'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")