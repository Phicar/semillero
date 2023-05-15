a = int(input())
for aa in range(a):
	b = int(input())
	if b&(b-1)==0:
		print("NO")
	else:
		print("YES")
