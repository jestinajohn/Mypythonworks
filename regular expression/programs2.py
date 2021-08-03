# import re
# x='[a-zA-Z0-9]+[@]+[a-z]+[.]+[a-z]+'
# st=input("enter mail id")
# match=re.fullmatch(x,st)
# if match !=None:
#     print("valid")
# else:
#     print("invalid")

# import re
# f1=open('f1','r')
# x='[+][9][1]\d{10}$'
# for i in f1:
#     data=i.rstrip("\n")
#     n=re.fullmatch(x,data)
#     if n!=None:
#         print(i)

# import re
# # f1=open('f1','r')
# # x='[+][9][1][0-9]{10}$'
# # for i in f1:
# #     data=i.rstrip("\n")
# #     n=re.fullmatch(x,data)
# #     if n!=None:
# #         print(i)


import re
st=input("enter string")
x='([A-Z]{1}[^a-zA-Z0-9]+[A-Z])?{4,6}'
n=re.fullmatch(x,st)
if n!=None:
    print("valid")
else:
    print("invalid")
