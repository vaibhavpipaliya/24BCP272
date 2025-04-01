import random
lst1=[random.randint(-15,15) for i in range(11)]
def fun(n):
    return n**2
m1=map(fun,lst1)
print(list(m1))
print(lst1)
