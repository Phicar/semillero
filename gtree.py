a = int(input())
b = map(int,raw_input().split(" "))
b.sort()
mm = a//2
x = sum(b[0:mm])
y = sum(b[mm:])
print(x*x+y*y)
