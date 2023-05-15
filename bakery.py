a = map(int,raw_input().split(" "))
res = -1
dic = {}
L = []
for i in range(a[1]):
	L.append(raw_input())
#for i in range(a[1]):
#	aa = map(int,raw_input().split(" "))
#	if aa[0] not in dic.keys():
#		dic[aa[0]]=[]
#	if aa[1] not in dic.keys():
#               dic[aa[1]]=[]
#	dic[aa[0]].append([aa[1],aa[2]])
#	dic[aa[1]].append([aa[0],aa[2]])
b = []
bb = set()
q = [False for i in range(a[0])]
if a[2]>0:
	b = map(int,raw_input().split(" "))
	bb = set()
	for x in b:
		q[x-1]=True
		bb.add(x)
for i in range(a[1]):
        aa = map(int,L[i].split(" "))
        if aa[0] not in dic.keys():
                dic[aa[0]]=10**21
        if aa[1] not in dic.keys():
                dic[aa[1]]=10**21
        c = 0
	for j in range(2):
		if q[aa[j]-1]:
			c+=1
	if c==1:
	        dic[aa[0]] = min(aa[2],dic[aa[0]]) #.append([aa[1],aa[2]])
        	dic[aa[1]] = min(aa[2],dic[aa[1]]) #.append([aa[0],aa[2]])
if a[2]>0:
	for x in b:
		if x in dic.keys():
			y = dic[x] #for y in dic[x]:
				#print(x,y)
			if y<res or (y<10**21 and res==-1):
				res = y
print(res)
