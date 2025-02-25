name={'A','B','Ab','BA'}
A=set()
B=set()
for i in name :
    for char in i:
        if i[0]=="A":
            A.add(i)
        elif i[0]=="B":
            B.add(i)
print(A,B)
