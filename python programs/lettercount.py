a="malayalam"
b= input("enter  letter")
c=0
for i in a:
    if i in b:
        c=c+1
if c==0:
    print(b," not present")
else:
 print(b," is present",c,"times")