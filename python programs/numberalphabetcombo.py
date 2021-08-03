str=input("enter a string")
num="0123456789"
c=0
count=0
st1=""
st2=""
for i in str:
    if i in num:
        c=c+1
        st1=st1+i
    else:
        count=count+1
        st2=st2+i
print("There are : ",c," numbers : ",st1)
print("There are : ",count," letters : ",st2)