a = int(input())
for cc in range(a):
	b= raw_input()
	t= 0
	for l in range(len(b)-1):
		if b[l]=='_' and b[l+1]=='_':
			t+=1
	if b[0]=='_':
		t+=1
	if len(b)>1 and b[-1]=='_':
		t+=1
	if len(b)==1:
		if b[0]=='_':
			t=2
		else:
			t=1
	print(t)
