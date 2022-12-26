def extract_consonants(s):
    n_consonants=0
    for i in s:
        if i in 'trqwdsjk':
            n_consonants+=1
    return n_consonants
str1=input()
a=extract_consonants(str1)
print("no of consonants in:'",str1,"' is",a)
