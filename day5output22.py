def extract_specialCharacters(s):
    n_specialCharacters=0
    for i in s:
        if i in '#$#$%^^&*()!@#':
            n_specialCharacters+=1
    return n_specialCharacters
str1=input()
a= extract_specialCharacters(str1)
print("no of specialCharacters in:'",str1,"' is",a)
