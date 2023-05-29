from re import I


n=int(input("enter a value for n:"))
s=0.0
for i in range(1,n+1):
    a=float(i**i)/i
    s=s+a
print("the sum of the series is",s)
