import random
a=set()
count=0
while len(a)<=10:
    b=random.randint(15,45)
    a.add(b)
print(a)
l=[]
for i in a:
    if i<30:
     count+=1
    elif i>35:
     l.append(i)
for i in l:
    a.remove(i)
print(a,count)

