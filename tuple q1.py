lst1=[("vaibhav",),("prince",),'x','y','z']
boys=0
girls=0
for i in lst1:
    if isinstance(i,tuple):
        boys+=1
    else:
        girls+=1

print(boys)
print(girls)


