# elements added into a list *****************************8

# a=[]
# n=int(input("no of elements to be added : "))
# while n>0:
#     d=input("element : ")
#     a.append(d)
#     n=n-1
# print(a)


# display sum and multiplication *****************************
# a=[1,2,3,4]
# sum=0
# m=1
# for i in a:
#     m=m*i
#     sum=sum+i
# print("sum : ",sum)
# print("multiplication : ",m)


# even number **************************

# a=[1,2,3,4]
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)


# check whether an element is present or not *********************

# a=[1,2,3,4,5,6,7,8]
# n=int(input("enter the element"))
# c=0
# for i in a:
#     if i==n:
#         print(n," is present")
#         c=c+1
#         break
# if c==0:
#     print("not present")



# sorting *****************************

# a=[1,3,2,58,32]
# a.sort()
# print(a)



# sorting with loop ************

# a=[1,3,2,58,32]
# print(a)
# s=[]
# temp=0
# while a:
#     temp=a[0]
#     for i in a:
#         if i<temp:
#             temp=i
#     s.append(temp)
#     a.remove(temp)
# print(s)



# a=[1,3,2,58,32]
# print(a)
# s=[]
# temp=0
# for j in a:
#     temp=j
#     for i in a:
#         if i<temp:
#             temp=i
#     s.append(temp)
#     a.remove(temp)
# print(s)

# lt=[1,2,3,4,5,6,7,5]
# # print(lt[2])
# # print(lt[-3])
# n=int(input("enter the index"))
# l=len(lt)
# if n>=l:
#     print("not present")
# else:
#     print(lt[n])


# minimum maximum **************
# a=[1,3,2,58,32,54,14]
# l=len(a)
# print(a)
# s=[]
# temp=0
# while a:
#     temp=a[0]
#     for i in a:
#         if i<temp:
#             temp=i
#     s.append(temp)
#     a.remove(temp)
# print("min = ",s[0],"\n","max = ",s[l-1])


# repeat element ******************************
# a=[1,2,2,3,4,3,5]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#     else:
#         print(i)

# multiply with 5 ****************

# a=[1,2,2,3,4,3,5]
# b=[]
# m=0
# for i in a:
#     m=i*5
#     b.append(m)
# print(b)


# list comprehension *********************************
# it is used for creating new lists from other iterables.
# As list comprehensions return lists,they consists of bracket  containing the expression,
# which is executed for each element along with the for loop to iterate over each element.

# specify conditions within the list using space

# a=[1,2,2,3,4,3,5]
# b=[i*5 for i in a]
# print(b)

# even number between 1 and 20 using list comprehension *************

# b=[i for i in range(1,20) if i%2==0 ]
# print(b)

# find all of the numbers from 1 to 1000 that are divisible by 8 ?

# b=[i for i in range(1,1000) if i%8==0 ]
# print(b)
# print(len(b))


# merge two list using extend keyword **************************

# lst=[1,2,3]
# b=[4,5,6]
# lst.extend(b)
# print(lst)


# repeat element elimination in single line code *************************

# a=[1,0,7,5,9,2,3,5,7,2,0,1,1,0]
# b=[]
# [b.append(x) for x in a if x not in b]
# print(str(b))

a=[1,2,3,33,2,5,4,6,4,5,3]
print(a[1])
# print(list(set(a)))