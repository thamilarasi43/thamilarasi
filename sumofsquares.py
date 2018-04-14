n1=int(input("enter num"))
b=0
while(n1!=0):
    a=n1%10
    b=b+(a*a)
    n1=n1//10
print(b)
