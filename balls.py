a = int(input())
for aa in range(a):
	b = map(int,raw_input().split(" "))
	si = False
	vec = 0
	while vec<10 and b[0]>0 and b[1]>0 and b[2]>0:
		vec+=1
		imp = 0
		for i in range(4):
			imp+=b[i]%2
		if imp<=1:
			si = True #print("YES")
			break
		else:
			b[0]-=1
			b[1]-=1
			b[2]-=1
			b[3]+=1
	imp = 0
	for ii in range(4):
		imp+=b[ii]%2
	if imp<=1:
		si = True
	if si:
		print("Yes")
	else:
		print("No")
