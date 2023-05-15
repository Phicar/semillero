a = int(input())
for aa in range(a):
	s1 = raw_input()
	s2 = raw_input()
	i = 0
	j = 0
	la = -1
	paila = False
	while j<len(s2):
		jj = j
		if i<len(s1) and s2[j]==s1[i]:
			j+=1
			la = s1[i]
			i+=1
		else:
			while j<len(s2) and s2[j]==la:
				j+=1
		if jj==j:
			paila = True
			break
		#if i==len(s1):
	if i<len(s1):
		paila = True
	if paila:
		print("NO")
	else:
		print("YES")
