#1
x,y = 10,20
print (x,y)

x,y = y,x
print (x,y)

#2
n = 10
result = 1 < n < 20
print (result)

result = 1 > n <= 9
print (result)

#3
x = 10 if y == 9 else 20

x = (classA if y == 1 else classB)(param1,param2)

def small(a,b,c):
	return a if a <= b and a <= c else (b if b <= a and b <= c else c)

print (small(1,2,0))
print (small(1,2,3))
print (small(20,39,3))


