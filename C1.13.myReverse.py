"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""


def myReverse(data):
    length = len(data)
    reverseData = []
    for i in range(length-1,-1, -1):
        reverseData.append(data[i])
    return reverseData

stringData = input("Enter the list of values with spaces ")
data = [int(x)  for x in stringData.split()]
print(myReverse(data))
print(data[::-1])