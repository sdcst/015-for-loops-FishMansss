#! python3
"""
##### Task 3
Print all the numbers from 1 to 1000 that are divisible by 5.
"""

for i in range(1001):
    x = i%5
    if x==0:
        print(i)
    