import random
lst1=random.sample(range(-100,100),30)
print("orignal list:",lst1)
positive=[num for num in lst1 if num >0 ]
print("positive numbers:",positive)
negative=[num for num in lst1 if num <0 ]
print("negative numbers:",negative)
