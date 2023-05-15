x =raw_input()
if len(x)>2:
	x = x[-2:]
xx = int(x)%4
print((1+2**xx+3**xx+4**xx)%5)

