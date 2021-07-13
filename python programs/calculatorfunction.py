def add(n1,n2):
    print(n1+n2)

def mult(n1,n2):
    print(n1*n2)

def sub(n1,n2):
    print(n1-n2)

def div(n1,n2):
    print(n1/n2)
print("Choose your options \n 1.ADD \n 2.SUB \n 3.MULT \n 4.DIV \n")
while True:
    opt = (input("  Enter your option here : "))
    if opt in ('1','2','3','4'):
        n1 = float(input("enter first number"))
        n2 = float(input("enter second number"))
        if opt=='1':
            add(n1,n2)
        elif opt=='2':
            sub(n1,n2)
        elif opt=='3':
            mult(n1,n2)
        elif opt=='4':
            div(n1,n2)
        break
    else:
        print(" undefined symbol")
    break