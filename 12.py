"""12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""
def palindrome(word):
    if word==word[::-1]:
        print("given word is palindrome")
    else:
        print("given word is not palindrome")
str=input("enter your string: ")
palindrome(str)

