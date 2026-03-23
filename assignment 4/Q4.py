#WAP TO CREATE A FUNCTION THAT PRINTS THE FIRST 15 TERMS OF THE FIBONNACI SERIES WITHOUT USIONG RECURSION 
def fibonacci(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
n=int(input("enter the number of terms you want to print:"))
print("the fibonacci series of first",n,"terms are:")
fibonacci(n)
