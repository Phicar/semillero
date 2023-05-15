def f(x):
	if x<=1:
		return x
	s = 0
	for k in range(1,x):
		s+=f(k)
	return s
print(f(10))
