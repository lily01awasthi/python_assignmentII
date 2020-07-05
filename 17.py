"""17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors."""
try:
    first_num = int(input("enter your 1st number: "))
    second_num = int(input("enter your 2nd number "))
except ValueError:
    print("please enter a integer.!")
oper=input("enter the operation you want to perform(+,-,*,/)")
if(oper=="+"):
    print(first_num + second_num)
elif(oper=="-"):
    print(first_num - second_num)
elif(oper=="*"):
    print(first_num * second_num)
elif(oper=="/"):
    try:
        print(first_num / second_num)
    except ZeroDivisionError:
        print("we can not divide a number by zero")
else:
    print("please enter a correct operator")