# adding extra features without changing function definition

# def check(fn):
#     def wrapper(name,age):
#         if age <18:
#             print("not eligible")
#         else:
#             return fn(name,age)
#     return wrapper
# @check
# def vaccine(name,age):
#     print(name,"eligible")
# vaccine("anu",17)



# def check(fn):
#     def wrapper(n1,n2):
#         if n1<n2:
#             (n1,n2)=(n2,n1)
#             return fn(n1,n2)
#     return wrapper
# @check
# def sub(n1,n2):
#     print("difference = ",n1-n2)
# sub(5,10)
