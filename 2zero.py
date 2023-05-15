c  = int(input())
for cc in range(c):
	aa = map(int,raw_input().split(" "))
	a = aa[0]
	b = aa[1]
	mini = 0
	maxi = a
	cad = -1
	while mini<=maxi:
		mid = (mini+maxi)//2
		if b<2*mid:
			maxi = mid-1
		if b>=2*mid:
			r = b-2*mid
			#print(mid,r,a,"=",mid+2*r,b,"=",2*mid+r)
			if 2*r+mid<=a:
				maxi = mid-1
				if 2*r+mid==a and b==2*mid+r:
					cad = mid
			else:
				mini = mid+1
	if cad ==-1:
		print("NO")
	else:
		print("YES")
