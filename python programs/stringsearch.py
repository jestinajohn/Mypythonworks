# a="luminar technology"
# for i in a:
#     print(i)



# a="luminar technology"
# b= input("enter  letter")
# c=0
# for i in a:
#     if i in b:
#         c=c+1
# if c==0:
#     print(b," not present")
# else:
#  print(b," is present",c,"times")



# if b in a:
#         c=c+1
# if c==0:
#     print(b," not present")
# else:
#  print(b," is present",c,"times")

str= input("enter  string")
b='''!@#$%^&*+`-="[]}\|;':,.<>/?'''
d=""
for c in str:
    if c not in b:
        d=d+c
print(d)



