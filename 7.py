"""7. Create a list of tuples of first name, last name, and age for your friends and colleagues.
If you don't know the age, put in None. Calculate the average age, skipping over any None values.
Print out each name, followed by old or young if they are above or below the average age.
"""
people=[]
age_sum=0
count=0
fren_count=int(input("enter the number of friends you have:"))
for i in range(fren_count):
    name=input(f"enter your {i+1} friend's first name:")
    caste=input(f"enter your {i+1} friend's last name:")
    age_count=input(f"enter your {i+1} friend's age:")
    try:
        age_count=int(age_count)
        count+=1
    except ValueError:
        age_count=None
    people.append((name,caste,age_count))
for i in people:
    if i[2] is not None:
        age_sum=age_sum+i[2]
avg_age=age_sum/count
for i in people:
    if i[2] is not None:
        if i[2]>avg_age:
            print(f"{i[0]} you got old")
        else:
            print(f"{i[0]} you 're still young")

