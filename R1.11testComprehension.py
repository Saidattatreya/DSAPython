"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""
list = [pow(2,y) for y in range(0,9)]
print(list)