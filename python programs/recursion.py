# recursion...a function call itself is called recursion
# def r(n):
#     if n<=1:
#         return n
#
#     else:
#         return r(n-1)+r(n-2)
# nterms=10
# print("fbonacci series")
# for i in range(nterms):
#     print(r(i))

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(10))