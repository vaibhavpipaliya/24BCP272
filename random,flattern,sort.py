import random
odd_num=random.sample(range(1,100,2),5)
print(odd_num)
even_num=random.sample(range(2,100,2),4)
print(even_num)
odd_num[2]=even_num
print(odd_num)

flattern=[]
for item in odd_num:
    if isinstance(item,list):
        flattern.extend(item)
    else:
        flattern.append(item)
print(flattern)        
flattern.sort()
print(flattern)
            
    
