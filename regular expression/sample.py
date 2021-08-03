# pattern matching ( a,b,c) ******************************************

# import re
# x='[abc]'
# matcher=re.finditer(x, "abt c@5kzabcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern matching ( except a,b,c) *************************************

# import re
# x='[^abc]'
# matcher=re.finditer(x, "abt c@5kzabcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern matching ( print lowercase)********************************8

# import re
# x='[a-z]'
# matcher=re.finditer(x, "abt c@5kzabcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# pattern matching ( print uppercase)****************************************

# import re
# x='[A-Z]'
# matcher=re.finditer(x, "abt c@5KZAbcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# pattern matching (print both lowercase and uppercase) *************************

# import re
# x='[a-zA-Z]'
# matcher=re.finditer(x, "abt c@5KZAbcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern matching (print digits) *************************

# import re
# x='[0-9]'
# matcher=re.finditer(x, "abt c@5KZ8Abcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern matching (print non digits) *************************

# import re
# x='[^0-9]'
# matcher=re.finditer(x, "abt c@5KZ8Abcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern matching (print symbols) *************************

# import re
# x='[^0-9a-zA-z]'
# matcher=re.finditer(x, "abt c@5KZ8Abcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern matching (check digits) *************************

# import re
# x='\d'
# matcher=re.finditer(x, "abt c@5KZ8Abcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# pattern matching (check space) *************************

# import re
# x='\s'
# matcher=re.finditer(x, "abt c@5KZ8Abcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern matching (except digits) *************************

# import re
# x='\D'
# matcher=re.finditer(x, "abt c@5KZ8Abcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern matching (all wrods except special characters) *************************

# import re
# x='\w'
# matcher=re.finditer(x, "abt c@5KZ8Abcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern matching (for special characters) *************************

# import re
# x='\W'
# matcher=re.finditer(x, "abt c@5KZ8Abcd")
# for match in matcher:
#     print(match.start())
#     print(match.group())

