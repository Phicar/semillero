a =int(input())
for _ in range(a):
	b = raw_input()
	co = 0
	vis = [False for i in range(26)]
	mit = False
	for i in range(len(b)//2):
		if not vis[ord(b[i])-ord('a')]:
			co+=1
			vis[ord(b[i])-ord('a')]=True
	if len(b)%2<3:
		if co==1:
			print("NO")
		else:
			print("YES")
	#else:
	#	if co<=2 and :
	#	else:
	#		print("YES")
