from collections import deque
q = deque()
q.append(1)
q.append(2)
while len(q)>0:
	print(q.popleft())
