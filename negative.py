n1=int(input())
b=n1/2
c=0
d=0
for i in range(n1):
    a=int(input())
    if i<=b:
        c=c+a
    else:
        d=d+a
if c>d:
    print(c)
else:
    print(d)
