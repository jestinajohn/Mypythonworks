# queue
# inserion - enqueue
# deletion - dequeue
# FIFO


lst=[]
size=int(input("enter size"))
def add():
    num = int(input("enter element to be pushed"))
    lst.append(num)
def rem():
    for i in lst:
        lst.remove(i)
        break
    print("removed successfully")
def display():
    print(lst)
op=1
while op != 0:
    print("enter operations want to perform")
    op=int(input("1.push  2.pop  3.display 0.Exit"))
    if op==1:
        if len(lst)<size:
            add()
        else:
            print("stack over flow")
    elif op==2:
        if len(lst)>0:
            rem()
        else:
            print("empty stack")
    elif op==3:
        display()
    elif op==0:
        break
    else:
        print("undefined symbol")
