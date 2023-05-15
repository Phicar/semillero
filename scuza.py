a =int(input())
for cc in range(a):
	aa = map(int,raw_input().split(" "))
	b = map(int,raw_input().split(" "))
	c = map(int,raw_input().split(" "))
	bm = []
	sm = []
	mm = b[0]
	bm.append(mm)
	sm.append(mm)
	for x in range(1,len(b)):
		mm = max(b[x],mm)
		bm.append(mm)
		sm.append(sm[-1]+b[x])
	ans = []
	#print(bm)
	#print(sm)
	for k in range(len(c)):
		le = c[k]
		mini = 0
		maxi = len(b)-1
		la = -1
		while mini<=maxi:
			mid = (mini+maxi)//2
			#print(le,mid,bm[mid])
			if le>=bm[mid]:
				#print("Si",le,bm[mid])
				la = mid
				mini = mid+1
			else:
				maxi = mid-1
		if la==-1:
			ans.append("0")
		else:
			ans.append(str(sm[la]))
	print(" ".join(ans))
