s1=input("enter the string")
b=len(s1)//2
print(b)
for i in range(len(s1)):
    if i==b:
        print(s1[i])
        s2=s1.replace(s1[i],'*')
print(s2)
