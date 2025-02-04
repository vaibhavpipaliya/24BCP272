import random
lst1=[random.randint(1,10) for _ in range(20)]
print(lst1)
a=int(input("enter number:"))
positions=[index for index,value in enumerate(lst1)if value==a]
if positions:
    print(f"the {a} is found at index value:{positions}")
else:
    print("num is not in lst")
