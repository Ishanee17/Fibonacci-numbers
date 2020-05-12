#creating a new function named as fib(n)
def fib(n):
    n = int(input("enter the the number of terms in the series: "))
    a=0
    b=1
    if n==1:
        print(a)
    elif n==0:
        print("no series")
    elif n<0:
        print("wrong data-only positive numbers")
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c=a + b
        a=b
        b=c
        print(c)
    
fib(100)
