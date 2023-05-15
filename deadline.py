import math
cc = int(input())
for c in range(cc):
	a= map(float,raw_input().split())
	n = a[0]
	d = a[1]
	if (1.0-n)**2+4*(n-d)>=0:
		x = ((n-1) + math.sqrt((1.0-n)**2+4*(n-d)))/2.0
		y1 = math.ceil(x-1)
		y2 = math.floor(x)
		entre = False
		#print(x,(1-n)**2+4*(n-d),y1,y2)
		for i in range(max(int(y1)-1,0),int(y2)+2):
			y11 = i+math.ceil(d/(i+1.0))
		#y22 = y2+math.ceil(d/(y2+1))
			#print(i,y11,y11<=n)
			if y11<=n:
				entre = True
				print("YES")
				break
		if not entre:
			print("NO")
	elif n>=d:
		print("YES")
	else:
		print("NO")
