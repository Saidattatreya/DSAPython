"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.

Give a single command that computes the sum from above Exercise,relying
on Python’s comprehension syntax and the built-in sum function.
"""
def sumOfSquares(n):
    sum = 0
    for x in range(1,n+1):
        sum += x*x
    return sum


n = int(input("Enter value upto which sum of squares needs to be calculated"))
print("Sum of squares upto {0} is {1}".format(n, sumOfSquares(n)))
print("Sum of squares upto {0} is {1}".format(n, sum( x*x for x  in range(1,n+1))))