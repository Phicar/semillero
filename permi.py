a = int(input())
for iii in range(a):
	aa = map(int,raw_input().split(" "))
	bb = map(int,raw_input().split(" "))
	tal=[0 for i in range(aa[0])]
	if aa[1]==1:
		print("0")
		continue
	cu = 0
	for i in range(0,aa[1]):
		tt = []
		for j in range(i,aa[0],aa[1]):
			if (i+1)%aa[1]!= bb[j]%aa[1]:
				cu+=1
	if cu>2:
		cu = -1
	elif cu==2:
		cu = 1
	print(cu)

