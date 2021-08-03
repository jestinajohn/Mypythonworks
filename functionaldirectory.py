 # arguments - actual values
 # parameters - variables passed
 # *args act as tuple
 #**args act as dictionary
# **kwargs act as dicitonary



# sum ****************************

# def add(*arg):
#     print(arg)
#     sum=0
#     for i in arg:
#         sum+=i
#     print(sum)
# add(2,3,4,5,6)

# employee data **************************************

# def det(*args):                                             # tuple return
#     print(args)
# det(2,"anu","kochi",5000,"wipro")


# **args ,return dictionary, variables read as key and values***************************************


# def det(**args):                                             # dictionary return
#     print(args)
# det(id=2,name="anu",place="kochi",salary=5000,company="wipro")

# print particular data from dictionary ***********************************


# employee={1000:{"eid":1000,"ename":"ajay","salary":5000,"designation":"developer"},
#           1001:{"eid":1001,"ename":"vinu","salary":8000,"designation":"developer"},
#           1002:{"eid":1002,"ename":"chinju","salary":15000,"designation":"hr"},
#           1003:{"eid":1003,"ename":"riya","salary":35000,"designation":"analyst"}}
# # print(employee[1002]['ename'])
# id=int(input("enter id"))
# key=input("enter property - eid,ename,salary,designation")
# if id in employee and key in employee[id]:
#      print(employee[id][key])
# else:
#      print("invalid eid or property")



# users={1000:{"acno":1000,"pswd":"user1","balance":3000},
#           1001:{"acno":1001,"pswd":"user2","balance":4000},
#           1002:{"acno":1002,"pswd":"user3","balance":5000},
#           1003:{"acno":1003,"pswd":"user4","balance":6000}}
# if 1000 in users:
#     print(users[1000]["balance"])


#     # print paasword 1002
# a=users[1002]["pswd"]
# print(a)

# def authenticate(usr,pswd):
#     if usr in users:
#         if users[usr]["pswd"]==pswd:
#             print("success")
#         else:
#             print("invalid pswd")
#     else:
#         print("invalid acno")
#
# #authenticate(1002,"user5")
#
# def get_balance(acno):
#     if acno in users:
#         print(users[acno]["balance"])
#     else:
#         print("invalid acno")
#
# #get_balance(1002)





#
# def authenticate(**kwargs):
#     usr=kwargs["acno"]
#     pswd=kwargs["pswd"]
#     if usr in users:
#         if users[usr]["pswd"]==pswd:
#             print("success")
#         else:
#             print("invalid pswd")
#     else:
#         print("invalid acno")
#
# authenticate(acno=1002,pswd="user3")
#
# def get_balance(acno):
#     if acno in users:
#         print(users[acno]["balance"])
#     else:
#         print("invalid acno")
#
# #get_balance(1002)



# def add(*args,**kwargs):
#     print(args)
#     print(kwargs)
# add(1,2,3,4,key="jest")





# lst=[2,3,1,4,5,7,6,8,6]
# #lst.sort()
# # lst.sort(reverse=True)
# # print(lst)





# # class List:
# #     def sort(self,**kwargs):   # kwargs={"reverse=True,"key":lst[0]}

# lst.sort(reverse=True)
# print(lst)




# class Bank:
#     users={1000:{"acno":1000,"pswd":"user1","balance":3000},
#               1001:{"acno":1001,"pswd":"user2","balance":4000},
#               1002:{"acno":1002,"pswd":"user3","balance":5000},
#               1003:{"acno":1003,"pswd":"user4","balance":6000}}
#     session={}
#     def validate_account(self,accno):
#         if accno  in self.users:
#             return True
#         else:
#             return False
#
#     def authenticate(self,**kwargs):
#         acc_no=kwargs["acc_no"]
#         password=kwargs["password"]
#         user=self.validate_account(acc_no)
#         if user:
#             if password==self.users[acc_no]["pswd"]:
#                 self.session["user"]=acc_no
#                 return acc_no
#             else:
#                 return -1    # invalid password
#         else:
#                 return 0     #invalid account number
#
#     def balance_enquiry(self,acc_no):
#         if acc_no==self.session["user"]:
#             print(self.users[acc_no]["balance"])
#         else:
#             print("you must login")
#
#     def fund_transfer(self,user,to_acno,amt):
#         if self.validate_account(to_acno):
#             balance=self.users[user]["balance"]
#             if balance<amt:
#                 print("insufficient balance")
#             else:
#                 self.users[user]["balance"]-=amt
#                 self.users[to_acno]["balance"]+=amt
#                 print(self.users[to_acno]["balance"])
#                 print("your balance :",self.users[user]["balance"])
#
#     def logout(self):
#         self.session["user"]=0
#
# # obj=Bank()
# # user=obj.authenticate(acc_no=1002,password="user3")
# # obj.balance_enquiry(user)
#
# obj1=Bank()
# user=obj1.authenticate(acc_no=1003,password="user4")
# if (user==-1) | (user==0):
#     print("authentication failed")
# else:
#     obj1.balance_enquiry(user)
# obj1.fund_transfer(user,1000,2000)

# def get_balance(acno):
#     if acno in users:
#         print(users[acno]["balance"])
#     else:
#         print("invalid acno")
