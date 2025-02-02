#find the value of sinx
a=int(input("enter degree: "))
n=int(input("enter terms for calculate:"))
def fact(a):
    if  a>1:
         return a*fact(a-1)
    elif a == 1 or a == 0:
         return 1
def sinx(a,n):
        sine=0
        j=0
        for i in range (1,2*(n+1),2):
            s=(-1)**j
            sine+=s*((a*(22/7)/180))**i/fact(i)
            j+=1
        return round(sine,2)
print(sinx(a,n))
