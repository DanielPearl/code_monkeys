# Calculate the nth number in a fibonacci sequence
# fib = 0112358

def fib_r(n):
    """
    Calculates the nth number in fibonacci sequence
    :param n: int
    :return: int
    """
    if n is 0 or n is 1: return n
    else: return fib(0,1,1,n)

def fib(a, b, i, n):
    """
    Called by fib_r to recursively search nth number in fib sequence
    :param a, b, i, n: int
    :return: int
    """
    if i >= n-1:
        return a + b
    else:
        c = a + b
        return fib(b, c, i+1, n)

def fib_it(n):
    """
    Calculates the nth number in fibonacci sequence
    :param n: int
    :return: int
    """
    if n is 0 or n is 1: return n
    a = 0
    b = 1
    c = None
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return c

print(fib_r(5))
print(fib_it(5))
