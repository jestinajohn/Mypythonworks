
#calculate sum of elements in a tuple  ******************

# tp=2,4,5,3,8,9
# sum=0
# l=len(tp)
# for i in range (0,l):
#     sum=sum+tp[i]
# print("sum = ",sum)

#calculate sum of elements in a tuple using tuple unpacking ******************

# tp=2,3,4,5
# a,b,c,d=tp
# sum=a+b+c+d
# print(sum)

# slicing *******************

# tp=4,3,5,6,7,8,9,5
# print(tp[1:4])
# print(tp[-2])
# print(tp[::-1])   # reversing ( palindrome problem )
# print(tp[::1])


# count and index in tuple *****************

# tp=(4,6,7,9,10,'hai',4)
# print(tp.count(4))
# print(tp.index(9))

# find first recursive element ********************

# st=input("Enter string")
# str=""
# c=0
# for i in st:
#     for j in st:
#         if i==j:
#             c=c+1
#         if c>1:
#             str=i
#             break
#     if c>1:
#         break
# print("repeat element",str)


# pattern=input("Enter string")
# count={}
# for i in pattern:
#     if i not in count:
#         count.update({i:1})
#     else:
#         print("first recursive element =",i)
#         break

# st=input("Enter string")
# c=0
# for i in st:
#     c=st.count(i)
#     if c>1:
#         break
# print("first recursive element =",i)