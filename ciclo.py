import math
def tal(n):
	radd = 2*math.pi/360
	ang = 360.0/(2.0*n)
	s = 0
	for i in range(1,n//2+n%2):
		#print(n,i,math.sin(ang*i*radd),math.cos(180+ang*(i+2)*radd)*2)
		s+=abs(math.sin(ang*i*radd))
	return 2*s+1.0
n = int(input())
for i in range(n):
	a = int(input())
	print("{:.9f}".format(tal(a)))

