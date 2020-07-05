"""
20. Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3,-10]]
"""
import itertools
lis=[-25, -10, -7, -3, 2, 4, 8, 10]
for i in range(0, len(lis)+1):
    for subset in itertools.combinations(lis, 3):
        if sum(subset)==0:
            print(subset)
def sum(lis):
    sum=0
    for i in lis:
        sum+=i
    return sum