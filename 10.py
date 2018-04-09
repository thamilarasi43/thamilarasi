def stair():
	s1=0
	l=[]
	n=int(input())
	for i in range(n):
		l.append(int(input()))
	for i in l:
		s1+=(n-i)
	print(s1)
try:
  stair()
except:
  print('invalid')
