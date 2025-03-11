def count_upper_lower():
    a=input("enter string : ")
    count=0
    count1=0
    for char in a:  
        if char.isupper():
            count+=1
        elif char.islower():
            count1+=1
    
    b={"upper":{count},"lower":{count1}}
    print(b)
count_upper_lower()        

