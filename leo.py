a = int(input())
neg = a<0
a = abs(a)
if not neg:
	print(a)
else:
	aa = str(a)
	b = int(str(a)[:-1])
	c = int(aa[:-2]+aa[-1])
	if b<c:
		print(-b)
	else:
		print(-c)
