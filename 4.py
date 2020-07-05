"""4. Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort
 the list. What is the first item on the list? What is the second item on the list?"""
friends=['asim','hitesh','puru','sabina','sanju']
list_id=id(friends)
name=input("enter your friend's name: ")
friends.append(name)
if id(friends)==list_id:
    print("list id is same")
else:
    print("list id is not same")
sorted_list=friends.sort()
print(f"first item on the list:{friends[0]}")
print(f"second item on the list:{friends[1]}")
