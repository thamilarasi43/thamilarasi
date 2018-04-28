s=['a','e','i','o','u']
s1=input("enter the string")
l1=[]
for i in range(len(s1)):
    if s1[i] not in s:
      l1.append(s1[i])
a=l1[::-1]
print(str(a))
