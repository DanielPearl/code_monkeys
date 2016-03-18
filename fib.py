# fib = 0112358

def fib_r(n):
    if n is 0 or n is 1: return n
    else: return fib(0,1,1,n)

def fib(a, b, i, n):
    if i >= n-1:
        return a + b
    else:
        c = a + b
        return fib(b, c, i+1, n)

print(fib(0, 1, 0, 10))
# for i in range(10):
#     print(fib_r(i))

def fib_it(n):
    if n is 0 or n is 1: return n
    a = 0
    b = 1
    c = None
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return c

# for i in range(1000):
#     print(fib_it(i))
