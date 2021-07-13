a = "abc"
b = "abds"

for i in a:
    if i not in b:
        print(i)

for i in b:
    if i not in a:
        print(i)

