# employees={1000:{"id":1000,"name":"Ajay","desig":"developer","exp":2,"salary":25000}}
f1=open("exam","r")
employees={}
for line in f1:
    eid,name,desig,exp,salary=line.rstrip("\n").split(",")
    employees[int(eid)]={"eid": eid,"name": name,"desig": desig,"exp": exp,"salary": salary}
print(employees)
def printEmployee(id=None,**kwargs):
    if id in employees:
        print(employees[id]["name"])
        if "prop" in kwargs:
            print(employees[id][kwargs["prop"]])
    else:
        print("invalid id")


id=int(input("Enter id"))
printEmployee(id)
printEmployee(id,prop="salary")







# def details(id,**kwargs):
#
#     if id in emp:
#         print(emp[id]["name"])
#     else:
#         print("invalid ID")
# details(1000)
#
# def show(**kwargs):
#     id=kwargs["id"]
#     prop = kwargs["prop"]
#     if id in emp:
#         print(emp[id]["name"],emp[id][prop])
# show(id=1001,prop="salary")