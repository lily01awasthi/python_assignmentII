"""10. Write a function that takes camel-cased strings (i.e. ThisIsCamelCased),
 and converts them to snake case (i.e. this_is_camel_cased). Modify the function by adding an argument, separator,
 so it will also convert to the kebab case (i.e.this-is-camel-case) as well.
"""
str=input("enter a string you want to change the casing of: ")
strnew=""
separator=input("enter a separator: ")
for i in str:
    if i.isupper():
        if str.find(i)!=0:
            x=separator+i.lower()
            strnew+=x
        else:
            strnew+=i.lower()
    else:
        strnew+=i
print(strnew)
