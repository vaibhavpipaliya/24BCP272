import operator
lst=[("panipuri",100),("pizza",600),("puff",50),("chole_kulcha",80)]
for i in range(len(lst)):
    sorted(lst,key=operator.itemgetter(1))

    
print(sorted(lst,key=operator.itemgetter(1)))         
