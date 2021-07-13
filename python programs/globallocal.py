def fn1():
    global x,a
    a=4
    x=10
    print(a,x)
fn1()
x=x+2
print(a,x)