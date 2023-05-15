a = int(raw_input())
for i in range(a):
	l = int(input())
	s = raw_input()
	si = True
	for j in range(l//2+l%2):
		aa = ord(s[j])
		bb = ord(s[len(s)-1-j])
		if aa==bb or abs(aa-bb)==2:
			si = True
		else:
			si = False
			break
	if si:
		print("YES")
	else:
		print("NO")
