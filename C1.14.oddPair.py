"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
Solution:
Odd * Odd = Odd
Odd * even = even
So to have a distinct pair of numbers whose product is odd, we should have atleast
two odd numbers
"""
def oddPair(data):
    count = 0
    for x in data:
        if x%2 != 0:
            count += 1
    return True if count>1 else False

stringData = input("Enter the list of values with spaces ")
data = [int(x)  for x in stringData.split()]
print("We have Odd Pair " if oddPair(data) else "We do not have Odd Pair")


