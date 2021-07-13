a="abcdefg"
b="xxxa"
c=0
# for i in a:
#     for y in b:
#         if i in y:
#             c=c+1
#
# if c==0:
#     print("no common letters")
# else:
#  print(c," common letters")
for i in a:
    if i in b:
        print(i)
        c=c+1
if c==0:
    print("no common elements")

