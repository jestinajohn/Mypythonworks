n= int(input("enter number"))
a = 0
b = 1
sum = 0
print(a)
for i in range (n):
    a=b
    b=sum
    sum=a+b
    print(sum)
