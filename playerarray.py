def printArray(r, n1):
    for i in range(0,n1):
        print ("%d"%( r[i]),end=" ")
r = [243, 140, 240, 141, 142, 46, 74]
n1 = len(r)
pancakeSort(r, n1);
print ("Sorted Array ")
printArray(r,n1)
