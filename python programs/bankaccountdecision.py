fd=50000
print("WELCOME")
amount=int(input("enter the amount to be withdrawed"))
if amount>fd:
    print("not sufficient balance")
else:
    fd-=amount
    print("successfully withdrawed \ncurrent balance is",fd)