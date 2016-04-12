#Binary search algorithm O(log n)
import random

# function to generate array of random ints
def rand(n = 20):
    """
    Generates random list of ints up to given param
    :param n: int
    :return: list
    """
    a = []
    for i in range(20):
        a.append(random.randint(0,100))
    a.sort()
    return a

# generate sorted array of random ints
n = rand()
num = random.randint(0,100)

def search(num, a):
    """
    Rercursively searches for a random int in a randomly generated list (binary search)
    :param num: int
    :param a: list
    """
    print("Looking for " + str(num) + " in " + str(a))

    if len(a) > 1:
        mid = len(a)//2
        if num == (a[mid]):
            return True
        elif num < (a[mid]):
            return search(num, a[:mid])
        elif num > (a[mid]):
            return search(num, a[mid:])
        else:
            return False
    return False

print(search(num,n))
