"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

def is_Even(a):
    #Solution 1 -> Divide by 2
    return True if(a%2 == 0 and a>1) else False


def is_Even1(a):
    #Solution 2 -> Count
    return_val = True
    if a>0:
        for i in range(1,a+1):
            return_val = not return_val
    else:
        return False
    return return_val


def is_Even2(a):
    #Solution 3 -> Bitwise operator
    return (a>0) and (not(a&1))

a = int(input("Enter the number to check for Even: "))
print("{0} is Even Number".format(a) if is_Even(a) else "{0} is not an Even Number".format(a))
print("{0} is Even Number".format(a) if is_Even1(a) else "{0} is not an Even Number".format(a))
print("{0} is Even Number".format(a) if is_Even2(a) else "{0} is not an Even Number".format(a))