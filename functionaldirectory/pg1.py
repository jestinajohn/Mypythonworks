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