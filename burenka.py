c =int(input())
def gcd(a,b):
	if b==0:
		return a
	if a%b==0:
		return b
	return gcd(b,a%b)
for cc in range(c):
	a = map(int,raw_input().split())
	gc1 = gcd(a[0],a[1])
	gc2 = gcd(a[2],a[3])
	a[0]/=gc1
	a[1]/=gc1
	a[2]/=gc2
	a[3]/=gc2
	#print(gc1,gc2,a)
	if a[0]==a[2] and a[1]==a[3]:
		print 0
		continue
	if a[0]==0 or a[2]==0:
		print 1
		continue
	if a[0]%a[2]==0 and a[3]%a[1]==0:
		print 1
		continue
	if a[2]%a[0]==0 and a[1]%a[3]==0:
		print 1
		continue
	print 2
