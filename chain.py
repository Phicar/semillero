c = int(input())
for cc in range(c):
	a = int(input())
	print(a)
	p = [str(i+1) for i in range(a)]
	for j in range(a-1):
		print " ".join(p)
		p[j],p[j+1]=p[j+1],p[j]
	print " ".join(p)
