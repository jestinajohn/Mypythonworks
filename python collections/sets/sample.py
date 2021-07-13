# s={1,2,3,4,5,6,7,8,9,0}
# sq=set()
# sqt=0
# print(s)
# for i in s:
#     sqt=i*i
#     sq.add(sqt)
# print(sq)


# s={1,2,3,4,5,6,7,8,9,0}
# print(s)
# s.remove(0)     # removes specific elements
# print(s)
# s.clear()        # remove all elements
# print(s)
# del s           # delete set
# print(s)

# set1={1,2,3,4,5,6,7,8,9,0,8,78,65,43,56,23,14,63,78}
# print(set1)
# odd=set()
# even=set()
# for i in set1:
#     if i%2==0:
#         even.add(i)
#     else:
#         odd.add(i)
# print(even)
# print(odd)


# set1={1,2,3,4,5,6,7,8,9,0,8,78,65,43,56,23,14,63,78}
# s2={1,2,3,4,12,13,14}
# for i in set1:
#     if i in s2:
#         print(i)

# set1={1,2,3,4,5,6,7,8,9}
# print(set1)
# pr=set()
# npr=set()
#
# for i in set1:
#     if i >1:
#         for j in range (2,i):
#             if (i%j)==0:
#                 npr.add(i)
#                 break
#         else:
#             pr.add(i)
# print(pr)
# print(npr)

# a=set()
# n=int(input("no of elements to be added"))
# for i in range(0,n):
#     d=int(input("element :"))
#     a.add(d)
# print(a)