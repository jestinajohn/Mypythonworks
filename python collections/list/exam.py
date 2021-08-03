
lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
res=[]
c=0
for i in lst:
    for j in lst:
        if i==j:
            c=c+1
    if c==1:
        res.append(i)
print(res)


keep order
support duplicate elements
hetrogeneous
mutable



doesnot store duplicate elements
order doesnot keep
support hetrogenius data
mutable
nesting is not possible



a=[1,2,2,3,4,3,5]
b=[]
m=0
for i in a:
    m=i*5
    b.append(m)
print(b)