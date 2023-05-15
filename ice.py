a = int(input())
def find(x):
	if x==pad[x]:
		return x
	return find(pad[x])
def union(x,y):
	px = find(x)
	py = find(y)
	pad[py]=px
tal =[]
pad = [i  for i in range(a)]
for xx in range(a):
	aa = map(int,raw_input().split(" "))
	tal.append(aa)
for x in range(a):
	for y in range(x+1,a):
		if tal[x][0]==tal[y][0] or tal[x][1]==tal[y][1]:
			union(x,y)
cc = 0
for i in range(a):
	if i==pad[i]:
		cc+=1
print(cc-1)
