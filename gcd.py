def hcf(n,n2):
	while(n2!=0):
		t=n2
		n2=n%n2
		n=t
	return n
def main():
	n1=int(input())
	q=int(input())
	(l,r)=([],[])
	for i in range(n):
		l.append(int(input()))
	print(l)
	for c in range(q):
		n=int(input())
		n2=int(input())
		r.append(hcf(l[n-1],l[n2-1]))
	for i in r:
		print(r)
try:
  main()
except:
  print('invalid')
