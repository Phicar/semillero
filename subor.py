a = int(input())
for i in range(a):
	b = int(input())
	per = [i+1 for i in range(b)]
	si = True
	#for i in range(0,b):
	#	for j in range(i,b):
	#		tm = 0
	#		for k in range(i,j+1):
	#			tm|=per[k]
	#		print(i,j,tm,j-i+1)
	#		if tm<j-i+1:
	#			si = False
	if not si:
		print("------")
	print(" ".join(map(str,per)))
