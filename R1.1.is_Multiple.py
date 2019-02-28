def is_Multiple(m,n):
    return True if (n & m%n == 0) else False


m = int(input("Enter The number A: "))
n = int(input("Enter the number B: "))

print("{0} is multiple of {1}".format(n,m) if is_Multiple(m,n) else "{0} is not a multiple of {1}".format(n,m))