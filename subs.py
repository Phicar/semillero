a = int(input())
for i in range(a):
	b = map(int,raw_input().split(" "))
	b.sort()
	res = 0
	while b[0]>0:
		q = (int)(b[1]/(1.0*b[0])-1.0);
		#(k+1)b[0]<b[1]
		res+=q
		b[1]-=b[0]*q
		if b[1]>=b[0]:
			b[1]-=b[0]
			res+=1
		#print(b)
		b.sort()
	print(res)
