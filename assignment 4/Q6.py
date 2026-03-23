#wap TO CALC FACTORIAL OF A NUMBER USING RECURSION 
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
n=int(input("enter a number"))
if(n<0):
    print("it is a negative number:")
else:
    print("factorial of",n,"is:",factorial(n))
