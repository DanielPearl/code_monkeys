import random

# function to generate array of random ints
def rand(n = 20):
 a = []
 for i in range(20):
   a.append(random.randint(0,100))
   a.sort()
 return a

# generate sorted array of random ints
n = rand()
num = random.randint(0,100)
def search(num, a):
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
    else:
        return False


print(search(num,n))
