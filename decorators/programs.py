# change pin and delete account **************************
# def admin_required(func):
#     def wrapper(user,pin):
#         if user!="admin":
#             raise Exception("you are not allowed")
#         else:
#             return func(user,pin)
#     return wrapper
# @admin_required
# def change_pin(user,pin):
#     mypin=pin
#     return mypin
# @admin_required
# def delete_ac(user,acno):
#     return str(acno)+"delete"
# print(change_pin("admin",1000))
# print(delete_ac('user1',1000))
# print(delete_ac('admin',1000))

# def dec(fun):
#     def wrapper(num1,num2):
#         if num1<num2:
#             (num1,num2)=(num2,num1)
#         return fun(num1,num2)
#     return wrapper
# @dec
# def sub(num1,num2):
#     return num1-num2
# print(sub(5,6))


# division ********************************

def dec(fun):
    def wrapper(num1,num2):
        if num1<num2:
            return fun(num2,num1)
        else:
            return fun(num1, num2)
    return wrapper

def dect(fun):
    def wrapper(num1,num2):
        if (num1==0) | (num2==0):
            raise Exception("invalid")
        else:
            return fun(num1,num2)
    return wrapper

@dect
def sub(num1,num2):
    return num1/num2
try:
    print(sub(10,0))
except Exception as e:
    print(e.args)

