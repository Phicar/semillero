nn = int(input())
ady = [[0 for j in range(3)] for i in range(3)]
ady[0][1] = ady[1][0] =int(input())#1-2

ady[0][2] =ady[2][0] = int(input())#1-3
ady[2][1] =ady[1][2] = int(input())#2-3
act = 0
res = 0
mini = 1900000
mind = -1
for i in range(nn-1):
	for j in range(3):
		if act==j:
			continue
		if mini > ady[act][j]:
			mini = ady[act][j]
			mind = j
	#print(act,mind)
	res+=mini
	act = mind
print(res)
