s1=int(input("enter s1 score"))
s2=int(input("enter s2 score"))
s3=int(input("enter s3 score"))
s4=int(input("enter s4 score"))
s5=int(input("enter s5 score"))
tot=s1+s2+s3+s4+s5
average=tot/3
print("total score =",tot)
print("average score =",average)
if tot>=80:
    print("A Grade")
elif tot>=60:
    print("B Grade")
elif tot>=40:
    print("C Grade")
elif tot<40:
    print("D Grade")