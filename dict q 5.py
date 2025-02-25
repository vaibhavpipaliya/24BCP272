dict1={"potato":20,"tomato":10,"banana":15}
d2={"potato":5,"tomato":10,"banana":2}
total_bill=0
for i in dict1:
    for j in d2:
        if i==j:
            total_bill+=dict1[i]*d2[j]
print(total_bill)        
