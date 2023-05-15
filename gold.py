a = int(input())
si = False
def hagale(a,b):
	global si
	if si:
		return
	if a==b:
		si = True
		return
	if a<b:
		return
	if a%3!=0:
		return
	hagale(2*(a/3),b)
	hagale(a/3,b)
for _ in range(a):
	b = map(int,raw_input().split(" "))
	si = False
	hagale(b[0],b[1])
	if si:
		print("YES")
	else:
		print("NO")
