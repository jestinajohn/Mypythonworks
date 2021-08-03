# QUANTIFIERS *********************


# print a including group ***********************

# import re
# x='a+'
# st="abt aa Ab"
# matcher=re.finditer(x, st)
# for match in matcher:
#     print(match.start())
#     print(match.group())


#print count including zero number ************************

# import re
# x='a*'
# st="abt aa Ab"
# matcher=re.finditer(x, st)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# print count a as each including zero no of a ***************

# import re
# x='a?'
# st="abt aa Ab"
# matcher=re.finditer(x, st)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# print 2 no of a position ********************************************

# import re
# x='a{2}'
# st="abt aa Ab"
# matcher=re.finditer(x, st)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# print minimum 1 a and maximum 3 a ************************

# import re
# x='a{1,3}'
# st="abt aa aaa Ab"
# matcher=re.finditer(x, st)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# print check starting with a (starting of the string) ************************

# import re
# x='^a'
# st="abt aa aaa Ab"
# matcher=re.finditer(x, st)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# print check ending with a (end of the string) ************************

import re
x='a$'
st="abt aa aaa Aba"
matcher=re.finditer(x, st)
for match in matcher:
    print(match.start())
    print(match.group())