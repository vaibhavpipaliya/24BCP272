def simple(x):
    lst1=[n**1 for n in range(1,x+1)]
    squares=[n**2 for n in range(1,x+1)]
    qube=[n**3 for n in range(1,x+1)]
    tuple1=(lst1,squares,qube)
    return(tuple1)
    
    
a=int(input("enter digit : "))
simple(a)
print(tuple1)
