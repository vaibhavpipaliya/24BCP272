a=int(input("enter the integer upto Fibonacci series print : "))
x,y,sum=0,1,0
while sum<a:
    sum=x+y
    print(sum)
    x=y
    y=sum
