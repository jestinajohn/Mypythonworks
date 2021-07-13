
b= input("enter  string")
c=0
for i in b:
    if i in "aeiouAEIOU":
        c=c+1

if c==0:
    print(" no vowels")
else:
 print(c, "vowels")