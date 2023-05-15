import io,os,sys
input =io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
a = int(input())
for c in range(a):
	aa = input()[:-1] #raw_input()
	bb = input()[:-1] #raw_input()
	#print(aa,bb)
	if aa[0]==bb[0] or aa[-1]==bb[-1]:
		print("YES")
		if aa[0]==bb[0]:
			sys.stdout.write(aa[0]+"*\n") #print(aa[0]+"*")
		else:
			sys.stdout.write("*"+aa[-1]+"\n")
		continue
	si = False
	for i in range(0,len(aa)-1):
		t = aa[i:i+2]
		if si:
			break
		for j in range(0,len(bb)-1):
			if not si and  bb[j]==aa[i] and bb[j+1]==aa[i+1]:
				#print(c,aa,bb,j,j+2)
				si = True
				sys.stdout.write("YES\n")
				sys.stdout.write("*"+t+"*\n")
				break
	if not si:
		sys.stdout.write("NO\n")
