q = int(input())
for qq in range(q):
	aa = map(int,raw_input().split())
	k = aa[0]
	n = aa[1]
	a = aa[2]
	b = aa[3]
	mini = 0
	maxi = n
	cand = -1
	while mini<=maxi:
		mid = (mini+maxi)//2
		if k-mid*a>0:
			#print(mid,(n-mid))
			if k-mid*a-(n-mid)*b>0:
				#print(mid)
				cand = mid
				mini = mid+1
			else:
				maxi = mid-1
		else:
			maxi = mid-1
	if cand==-1 and k-n*b>0:
		cand = 0
	print(cand)
