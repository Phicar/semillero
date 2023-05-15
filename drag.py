aa =int(input())
for cc in range(aa):
	bb = map(int,raw_input().split(" "))
	cc = map(int,raw_input().split(" "))
	mini = 1
	maxi = bb[1]+1
	la = -1
	while mini<=maxi:
		mm = (mini+maxi)//2
		hh = mm
		for i in range(bb[0]-1):
			hh+=min(mm,cc[i+1]-cc[i])
		#print(mm,hh)
		if hh<bb[1]:
			mini = mm+1
		else:
			la = mm
			maxi = mm-1
	print(la)
