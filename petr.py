a = int(input())
si = False
b = []
for i in range(a):
	b.append(int(input()))
for x in range(1<<a):
	t = 0
	xx = x
	for i in range(a):
		if xx%2==1:
			t+=b[i]
		else:
			t-=b[i]
		xx//=2
	if t%360==0:
		print("YES")
		si = True
		break
if not si:
	print("NO")
