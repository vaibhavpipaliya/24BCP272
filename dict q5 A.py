dict1={"potato":20,"tomato":10,"banana":15}
d2={"potato":5,"tomato":10,"banana":2}
total_bill=0
bill={}
for k,v in dict1.items():
    if k in d2:
         bill[k]=v*d2[k]
         total_bill+=v*d2[k]
print(bill)
print(total_bill)        
