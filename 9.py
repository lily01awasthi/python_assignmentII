"""9. Write a binary search function. It should take a sorted sequence and the item it is looking for.
 It should return the index of the item if found. It should return -1 if the item is not found."""
lis=[]
num=int(input("enter the  number of items in the list:"))
for i in range(num):
    lis_item=int(input("enter the list items :"))
    lis.append(lis_item)
search_item=int(input("enter the item u wanna searchc for:"))
lis=sorted(lis)

def binary(lis,item):
    if item in lis:
        return (lis.index(item))
    else:
        return -1
status=binary(lis,search_item)
print(f"the index status is :{status}")