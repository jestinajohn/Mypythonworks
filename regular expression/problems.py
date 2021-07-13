

# check whether "helloo" is valid or not ******************************

# import re
# st="helloo"
# x='\w*'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# check whether "56kg" is valid or not ******************************

# import re
# st="56kg"
# x='[\d]{2}[k][g]'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# check whether string (aab6 , jjh5) is valid or not ******************************

# import re
# st=input("enter string")
# x='[a-zA-Z]+\d{1}$'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# check whether string (starting with a and ending with b) is valid or not ******************************

# import re
# st=input("enter string")
# x='^a[a-zA-Z0-9\W]*b$'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# check whether minimum length 8 and maximum 15,except numebrs******************************


# import re
# st=input("enter string")
# x='[\D]{8,15}'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# check whether starting with uppercase and remaining numbers,lowercase,symbols ******************************

# import re
# st=input("enter string")
# x='[A-Z]{1}[a-z0-9\W]+'                     # atleast  one character after uppercase,so we use + quantifier
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# phone number validation - 10 numbers

# import re
# st=input("enter number")
# x='[0-9]{10}'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# Indian phone number validation - 10 numbers with +91

# import re
# st=input("enter number")
# x='[+][9][1]\d{10}'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# vehicle reg number validation(KL08DF1234)

# import re
# st=input("enter reg number")
# x='[K][L]\d{2}[A-Z]{2}\d{4}$'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# read vehicle reg number from one file and write valid number into another file


# import re
# f1=open('f1','r')
# f2=open('f2','w')
# x = '[K][L]\d{2}[A-Z]{2}\d{4}$'
# for i in f1:
#     data = i.rstrip("\n")
#     match = re.fullmatch(x, data)
#     if match is not None:
#         f2.write(i)





# email validation ***********************import re
# f1=open('f1','r')
# f2=open('f2','w')
# x = '[K][L]\d{2}[A-Z]{2}\d{4}$'
# for i in f1:
#     data = i.rstrip("\n")
#     match = re.fullmatch(x, data)
#     if match is not None:
#         f2.write(data)
#         f2.write("\n")******************************

# import re
# st=input("enter mail id")
# x='\w+[@][a-z]+[.][a-z]+'
# match=re.fullmatch(x,st)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# print valid phone numbers from a file ***********************

# import re
# f1=open('f1','r')
# x = '[+][9][1]\d{10}'
# for i in f1:
#     data = i.rstrip("\n")
#     match = re.fullmatch(x, data)
#     if match !=None:
#         print(i)


# import re
# f1=open('f1','r')
# f2=open('f2','w')
# x = '[+][9][1]\d{10}'
# for i in f1:
#     data = i.rstrip("")
#     match = re.fullmatch(x, data)
#     if match is not None:
#         f2.write(i)



# move correct reg no from one file to another ***********************************


import re
f1=open('f1','r')
f2=open('f2','w')
x = "^LUM+\d{2}[P][Y]\d{3}$"
for i in f1:
    data = i.rstrip("\n")
    match = re.fullmatch(x, data)
    if match is not None:
        print(data)
        f2.write(data)
