a =int(input())
for cc in range(a):
	b = map(int,raw_input().split(" "))
	si = False
	for x in range(0,b[0]+1):
		if (x*(x-1))/2+((b[0]-x)*(b[0]-x-1))/2==b[1]:
			print("YES")
			si= True
			A = [str(-1) for xx in range(x)]
			for xx in range(b[0]-x):
				A.append(str(1))
			print(" ".join(A))
			break
	#a*(a-1)/2+b*b-1/2=k
	if not si:
		print("NO")
