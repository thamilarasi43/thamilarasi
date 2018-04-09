def pair():
	n1=int(input())
	l=[]
	f=0
	for i in range(n):
		l.append(int(input()))
	k=int(input())
	for i in range(n1-1):
		if l[i]==l[i+1]:
			s1=l[i]+l[i+1]
			if s1==k:
				f=1
				print('yes')
	if f!=1:
		print('no')
    
pair()
