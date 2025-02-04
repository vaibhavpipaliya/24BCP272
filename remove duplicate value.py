import random
lst1=[random.randint(1,30) for _ in range(50)]
print(lst1)
a=list(set(lst1))
print(a)