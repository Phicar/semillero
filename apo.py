print(1)
import random
for i in range(1):
	print(500000)
	ca = [str(random.randint((1<<60)-1,(1<<60))) for x in range(500000)]
	print(" ".join(ca))
