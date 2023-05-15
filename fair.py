a = int(input())
res = []
def si(a):
	b = str(a)
	for i in range(len(b)):
		if b[i]!='0' and a%int(b[i])!=0:
			return False
	return True
for aa in range(a):
	x = int(raw_input())
	for y in range(x,x+1000000):
		if si(y):
			print(y)
			#break
