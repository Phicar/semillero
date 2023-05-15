a = int(input())
r = [0,0,0]
for i in range(a):
	b = map(int,raw_input().split(" "))
	for j in range(3):
		r[j]+=b[j]
si = True
for i in range(3):
	if r[i]!=0:
		si = False
if si:
	print("YES")
else:
	print("NO")
