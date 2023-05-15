s = raw_input()
ss = raw_input()
if len(s)==len(ss):
	dif=[]
	#c = 0
	for i in range(len(s)):
		if s[i]!=ss[i]:
			dif.append(i)
	if len(dif)==0:
		print("YES")
	elif len(dif)==2:
		if s[dif[0]]==ss[dif[1]] and s[dif[1]]==ss[dif[0]]:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")
else:
	print("NO")
