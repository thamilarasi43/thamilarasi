n1=int(input("enter n1"))
q=int(input("enter q"))
l=[]
for i in range(n1):
    a=int(input("enter n1 val"))
    l.append(a)
for j in range(q):
    c1=0
    u=int(input())
    v=int(input())
    for i in range(u,v):
        c1=c1+int(l[i])
    print(c1)
