
# file read ********************************************

# file1=open('firstf','r')
# for i in file1:
#     print(i)

# file1=open('firstf','r')
# print(file1)

# file write ********************************************
# rewrite if give an existing filename
# create new file if give a new filename

# file1=open('secondf','w')
# file1.write(" luminar technology")

# copy content of one file into another file ************************

# file1=open('secondf','r')
# file2=open('thirdf','w')
# for i in file1:
#     file2.write(i)

# display word count of content in file ***********************

# file1=open('firstf','r')
# c=0
# dict={}
# for k in file1:
#     a = k.rstrip('\n').split(" ")
# for i in a:
#     c = 0
#     for j in a:
#         if i==j:
#             c=c+1
#
#     dict.update({i:c})
# print(dict)


#  Exception handling - solve unexpected errors ***************************
#  try block: exceptional code
#  catch block: solving code
#  finally : always execute whether exception occurs or not


# division by zero **********************************

# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# try:
#     print(num1/num2)
# except Exception as e:
#     print(e)
# finally:
#     print("inside finally block")


# list index out of range*************************

# a=[10,2,3,4]
# i=int(input("enter index"))
# try:
#     print(a[i])
# except Exception as e:
#     print(e)
# finally:
#     print("inside finally")

