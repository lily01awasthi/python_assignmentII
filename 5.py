""" 5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the corresponding information from your friends and append
them to the list. Sort the list. When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name, last name, or age.
"""
my_info=("Lalita","awasthi",23)
friend1=("jack","jonas",22)
friend2=("jane","tyler",24)
people=[]
people.append((my_info))
people.append(friend1)
people.append(friend2)
print(sorted(people))
print(sorted(people,key=lambda x:x[1]))
print(sorted(people,key=lambda x:x[2]))
