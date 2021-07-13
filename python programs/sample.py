n=5
for i in range(0,n):
    print(" "*(n-i),end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()