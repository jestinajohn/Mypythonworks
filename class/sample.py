
# empployee details **************************8
#
# class Employee:
#     def setval(self,name,id,salary,company):
#         self.id=id
#         self.name=name
#         self.company=company
#         self.salary=salary
#     def getval(self):
#         print("Name: ",self.name,'\n',"ID: ",self.id,"\n","company: ",self.company,"\n","SALARY: ",self.salary)
#
# obj=Employee()
# n=input("enter name")
# id=int(input("enter id"))
# company=input("enter company")
# salary=int(input("salary"))
# obj.setval(n,id,salary,company)
# obj.getval()



# addition *****************************************

# class Add:
#     def get(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def show(self):
#         print("sum=",self.num1+self.num2)
#         # print("difference=", self.num1 - self.num2)
#         # print("product=", self.num1 * self.num2)
#         # print("division=", self.num1 / self.num2)
# ob=Add()
# n1=int(input("enter first number"))
# n2=int(input("enter second number"))
# ob.get(n1,n2)
# ob.show()


# class Student:
#     def setval(self,name,rollno,mark,schoolname):
#
#         self.n=name
#         self.rollno=rollno
#         self.mark=mark
#         self.schoolname=schoolname
#
#         print("\n","Name: ",self.n,'\n',"Rollno: ",self.rollno,"\n","Mark: ",self.mark,"\n","Schoolname: ",self.schoolname)
#
# obj=Student()
# name=input("enter name")
# rollno=int(input("enter rollno"))
# mark=int(input("enter mark"))
# schoolname=input("schoolname")
# obj.setval(name,rollno,mark,schoolname)

# bank account*********************************************

# class Bank:
#
#     def trans(self,cash,opt):
#         amount = 50000
#         self.a=amount
#         self.cash=cash
#         self.opt=opt
#         if opt==1:
#             print("balance= ",self.a-self.cash)
#         elif opt==2:
#             print("balance= ", self.a + self.cash)
#         else:
#             print("undefined symbol")
# ob=Bank()
# print("1. withdraw \n 2. deposit")
# opt=int(input("choose option :"))
# cash=int(input("enter amount"))
# ob.trans(cash,opt)


# book class *********************************

# class Book:
#     lname="COLLEGE MAIN LIBRARY"        # static variable
#     def setval(self,bname,author,pages):
#         self.bname=bname
#         self.author=author
#         self.pages=pages
#
#         print("BOOK NAME: ",self.bname,"\n","AUTHOR : ",self.author,"\n","TOTAL PAGES : ",self.pages,"\n","LIBRARY NAME : ",Book.lname)
# ob=Book()
# ob.setval("C PROGRAMMING","DENNIS RICHIE",200)


# employee details static variable **************************8
#
class Employee:
    company="WIPRO"
    def setval(self,name,id,salary):
        self.id=id
        self.name=name

        self.salary=salary
    def getval(self):
        print("Name: ",self.name,'\n',"ID: ",self.id,"\n","company: ",Employee.company,"\n","SALARY: ",self.salary)

obj=Employee()
n=input("enter name")
id=int(input("enter id"))
salary=int(input("salary"))
obj.setval(n,id,salary)
obj.getval()
