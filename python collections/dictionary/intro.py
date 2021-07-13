 # dictionary is always key and value
 # mutable
 # nesting possible
 # repetition not possible

# dict={'Name':'zara','Age':23,'class':'first'}
# print(dict)
# print(type(dict))
# print("dict['Name']:", dict['Name'])
# print("dict['Age']:", dict['Age'])

# empty dictionary
# dict{}

# dict={'Name':'zara','Age':23,'class':'first'}

# dict['Age']=25                          # update existing entry
# dict['school']='abc school'             # addnew entry in two way
# dict.update({'location':'kochi'})
# print(dict)

# del dict['class']      removing entry with key
# print(dict)
# dict.clear()           remove all entries
# print(dict)
# del dict               delete entire dictionary
# print(dict)

# d={1:2,3:4}
# print(d)
# d.update({5:6})
# print(d)

# splitting *****************
# a="hello world"
# b=a.split(" ")
# print(b)
# for i in b:
#     print(i)

# count of words method 1 ************************************************

# st=input("enter string: ")
# a=st.split(" ")
# dict={}
# c=0
# for i in a:
#     c = 0
#     for j in a:
#         if i==j:
#             c=c+1
#
#     dict.update({i:c})
#
# print(dict)

# count of words method 2 ************************************************

# st=input(" > ")
# words=st.split(" ")
# dict={}
# for i in words:
#     count=words.count(i)
#     dict.update({i:count})
#
# print(dict)

a={1:2,2:{7:9}}
print(a)