#WAP TO CRTEATE AN INTEGER LIST OF 20 ELEMEMYS INCREASE THE ODD VALUED ELEMENT BY 5
s=[]
x=int(input("enter a element"))
for i in range(x):
    n=int(input("enter a elememt"))
    s.append(n)
for i in range(x):
    if s[i]%2!=0:
        s[i]=s[i]+5
print(s)
