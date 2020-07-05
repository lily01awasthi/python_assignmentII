"""19. Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid"""

class check_paranthesisi:
    str= input("enter your paranthesis: ")
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = []
    for i in str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                print ("Unbalanced paranthesis")
    if len(stack) == 0:
        print ("balanced paranthesis")
    else:
        print ("Unbalanced paranthesis")

