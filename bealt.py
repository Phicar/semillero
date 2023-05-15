a =int(input())
for aa in range(a):
	b = int(input())
	c = raw_input()
	iz = 0
	der =0
	dos = 0
	tog = 0
	for i in range(b):
		if c[i]=='-':
			iz+=1
			der+=1
			dos+=1
			if c[(i+1)%b]=='-':
				tog+=1
		elif c[i]=='<':
			iz+=1
		else:
			der+=1
	if der<b and iz<b:
		print(2*dos-tog)
	else:
		print(b)
