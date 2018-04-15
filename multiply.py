a1=int(input("enter num"))
b=1
c=0
while a1!=0:
    c=a1%10
    b=b*c
    a1=a1//10
print(b)
