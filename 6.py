"""6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""
friends=["mack","hery","joe","tyler","john"]
x=False
for i in friends:
    if(i=="john" ):
        x=True
        break
    else:
        x=False
if(x):
    print("john found")
else:
    print("not found")



