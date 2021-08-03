# 1. first type pattern

# *
# * *
# * * *
# * * * *
# * * * * *

# n=5
# for i in range (0,n):
#     for j in range (0,i+1):
#         print("*",end=" ")
#     print("")


# 2. second type
# * * * * *
# * * * *
# * * *
# * *
# *

# n=5
# for i in range (n,0,-1):
#     for j in range (0,i):
#         print("*",end=" ")
#     print("")

# 3.third type pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# n=5
# num=1
# for i in range (1,n):
#     for j in range (1,i+1):
#         print(num,end=" ")
#         num=num+1
#
#     print("")

# 4. fourth type pattern

# 1
# 1 2
# 1 2 3
# 1 2 3 4

# n=5
# for i in range (0,n):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print("")

# n=5
# for i in range (0,n):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print("")

# 5.fifth type pattern

# 1
# 2 2
# 3 3 3
# 4 4 4 4

# n=5
# num=0
# for i in range (0,n):
#     for j in range (1,i+1):
#         print(num,end=" ")
#     print("")
#     num=num+1

#
# 6 . pyramid
#
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *


# n=6
# k=n
# for i in range(0,n):
#     for r in range(0,k):
#         print(end=" ")
#     k=k-1
#     for j in range(0,i+1):
#         print("* ",end=" ")
#     print("\r")

# n=6
# k=n
# for i in range(0,n):
#     print(" " *(n-i), end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print("\r")


# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
#
# n=6
# k=2*n-1
# for i in range(n,0,-1):
#     for r in range(k,0,-1):
#         print(end=" ")
#     k=k+1
#     for j in range(0,i):
#         print("* ",end=" ")
#     print("\r")
#


#  7. trapizoid pattern
#
#       * * * * *
#      * * * * * *
#     * * * * * * *
#    * * * * * * * *
#   * * * * * * * * *
#  * * * * * * * * * *
#
#
# n=6
# k=n
# for i in range(0,n):
#     for r in range(0,k):
#         print(end=" ")
#     k=k-1
#     for j in range(0,i+5):
#         print("* ",end=" ")
#     print("\r")

#8. rectangle pattern

# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *

# n=5
# s=n
# for i in range (0,n):
#     for j in range(0,s):
#         print("* ",end=" ")
#     print()
#

# 9. parallelogram

# n=5
# s=n
# for i in range (0,n):
#     for k in range(0,s):
#         print(end=" ")
#     s=s+1
#     for j in range(0,n):
#         print("* ",end=" ")
#
#     print()

# n = 5
# s = n
# for i in range(0, n):
#     for k in range(0, s):
#         print(end=" ")
#     s = s - 1
#     for j in range(0, n):
#         print("* ", end=" ")
#
#     print()


n=5
def pattern(pp):
    for i in range (0,n):
        for j in range (0,i+1):
            print(pp,end=" ")
        print("")
def patt(pp):
    for k in range(n,0,-1):
        for h in range (0,k):
            print(pp,end=" ")
        print("")
limit=4
for a in range (1,limit+1):
    if a%2==0:
        patt(a)
    else:
        pattern(a)


