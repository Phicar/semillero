a =raw_input()
if a[0]!='-':
	print(a)
	quit()
if len(a)==2:
	print(0)
	quit()
a1 = int(a[:-1])
a2 = int(a[:-2]+a[-1])
if a1<a2:
	print(a2)
else:
	print(a1)

