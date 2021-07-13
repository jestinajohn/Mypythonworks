# lambda function

# add=lambda num1,num2:num1+num2
# print(add(2,3))

# find squares of all numbrs****************************8

# lst=[1,2,3,4,5,6,7]
# res=[]
# for i in lst:
#     res.append(i**2)
# print(res)


# def square(num):
#     return num**2


# map function *************************************************


# sq=list(map(square,lst))
# print(sq)

# sq=map(lambda num:num**2,lst)
# print(sq)


# sq=list(map(lambda num:num**2,lst))
# print(sq)

# print product name ****************************************************

# products=[{"item":"boost","mrp":290,"stock":50},
#           {"item":"bournvita","mrp":390,"stock":52},
#           {"item":"horlicks","mrp":240,"stock":54},
#           {"item":"complan","mrp":190,"stock":51},
#           {"item":"nutricharge","mrp":300,"stock":35}]
#
# # for i in products:
# #     print(i["item"])
#
# name=list(map(lambda i:i["item"],products))
# print(name)

# print even numbers********************************************************

# lst=[1,2,3,4,5,6,7,8,9]

# evens=list(filter(lambda num:num%2==0,lst))
# odd=list(filter(lambda num:num%2!=0,lst))
# print(evens)
# print(odd)

# print out of stock ****************************************************

# products=[{"item":"boost","mrp":290,"stock":50},
#           {"item":"bournvita","mrp":390,"stock":52},
#           {"item":"horlicks","mrp":240,"stock":54},
#           {"item":"complan","mrp":190,"stock":51},
#           {"item":"nutricharge","mrp":300,"stock":0}]
#
# for i in products:
#     if(i["stock"]==0):
#         print(i)

# stock=list(filter(lambda i:i["stock"]==0,products))
# print(stock)

# print all product details below 250 *************************************

# stock=list(filter(lambda i:i["mrp"]<=250,products))
# print(stock)

# lst=[2,3,4,8,10,7]  o/p [1,2,3,9,11,8] if num<5 num-1 else num+1 **************************

# lst=[2,3,4,8,10,7]
# res=list(map(lambda num:num+1 if num>5 else num-1,lst))
# print(res)

# evens=list(filter(lambda num:num%2==0,lst))
# for i in lst:
#     if i<5:
#         res.append(i-1)
#     else:
#         res.append(i+1)
# print(res)


# print,input,type,filter,sort,max,min   - builtins.py (import not needed)
# functools - reduce is in functools - it needed to import
# lambda has two variables

# from functools import reduce
# lst=[1,2,3,4,5,6,7]
# # tot=reduce(lambda num1,num2:num1+num2,lst)
# # print(tot)
# largest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
# print(largest)

# products **********************************************************************************

# from functools import reduce
# products=[{"item":"boost","mrp":290,"stock":50},
#           {"item":"bournvita","mrp":390,"stock":52},
#           {"item":"horlicks","mrp":240,"stock":54},
#           {"item":"complan","mrp":190,"stock":51},
#           {"item":"nutricharge","mrp":300,"stock":0}]
#
# prices=list(map(lambda product:product["mrp"],products))
# stock=reduce(lambda p1,p2:p1 if p1>p2 else p2, prices)
# print(stock)


lst=[1,2,3,4,5,6,7]
res=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
print(res)