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

[ m ** 2 if m > 10 else m ** 4 for m in range(50)]

#4
testList = [1,2,3]
x,y,z = testList
print (x,y,z)

#5
#打印模块的文件路径
import threading
import socket

print (threading)
print (socket)

#6
testDict = {i : i * i for i in xrange(10)}
testSet = {i * 2 for i in xrange(10)}

print (testDict)
print (testSet)

#7
#我们可以在pdb模块的帮助下在python脚本中设置断点

import pdb
pdb.set_trace()

#8
#开启文件共享
#python2
python -m SimpleHTTPServer

#python3
python3 -m http.server

#9
test = [1,2,3,4]
print (dir(test))


