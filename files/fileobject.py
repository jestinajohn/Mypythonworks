
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("NAME: ",self.name,"\nage: ",self.age)
    def __str__(self):
        return self.name
file1 = open('file1', 'r')
for i in file1:
    # print(i)
    data=i.rstrip("\n").split(",")
    print(data)
    name=data[0]
    age=data[1]
e=Employee(name,age)
# print(e)




