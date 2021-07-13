


# num1 = int(input("enter number"))
# c=0
# for i in range (2,num1):
#     if num1%i==0:
#         c+=1
# if c==0:
#     print("prime")
# else:
#     print("not prime")
#

num1 = int(input("enter initial range"))
num2 = int(input("enter  final range"))
c=0
sum=0
for j in range(num1,num2):
    if j>1:
        for i in range(2,j):
            if j%i==0:
                break
        else:
            print(j,"prime")
            sum=sum+j

print("sum = ",sum)

