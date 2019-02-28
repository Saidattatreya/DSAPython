def minMax(data):
    min = None
    max = None
    for a in data:
        if not min:
            min = a
        if not max:
            max = a
        if a < min:
            min = a
        if a > max:
            max = a

    return min,max


input_string = (input("Enter List of Values seperated by Spaces"))
data = [int(x) for x in input_string.split()]
min, max = minMax(data)
print("Minimum is {0} and \nMaximum is {1}".format(min,max))