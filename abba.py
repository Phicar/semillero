a = int(input())
for ii in range(a):
	b = raw_input()
	ab = 0
	ba = 0
	for i in range(len(b)-1):
		if b[i:i+2]=='ab':
			ab+=1
		elif b[i:i+2]=='ba':
			ba+=1
	s = ""
	l = 0
	if ab==ba:
		print(b)
		continue
	if ab<ba:
		l = ba-ab
		s = "ba"
	else:
		l = ab-ba
		s = "ab"
	bbb = ""
	for i in range(len(b)):
		if l>0 and i+2<=len(b) and b[i:i+2]==s:
			bbb+=s[1]
			l-=1
			#bbb+=s[1]
			#i+=1
		else:
			bbb+=b[i]
	print(bbb)

