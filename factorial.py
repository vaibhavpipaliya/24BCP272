

def factorial():
    a=int(input("enter number :"))
    factorial=1
    for i in range(1,a+1):
        factorial=factorial*i
   
    print("factorial of",a,"is",factorial)

factorial()
