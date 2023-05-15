aa = int(input())
for bb in range(aa):
	b = int(input())
	bx = map(int,raw_input().split(" "))
	c = int(input())
        cx = map(int,raw_input().split(" "))
	px = 0
	for i in range(b):
		px+=bx[i]%2
	qx = 0
	for i in range(c):
		qx+=cx[i]%2
	print(px*qx+(b-px)*(c-qx))
