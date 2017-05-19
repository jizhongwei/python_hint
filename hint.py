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

#10
if m in [1,2,3,4]:
if m in {1,2,3,4}:

#11
import sys
#detect the python version currently in use.
if not hasattr(sys,"hexversion") or sys.hexversion != 50660080:
	print ('sorry ,you aren\'t running on python 3.5n')
	print ("please upgrade to 3.5.n")
	sys.exit(1)

#print python version in a readable format.
print ("current python version:",sys.version)

#或者可以使用sys.version_info >= (3,5) 来替换上面代码的sys.hexversion != 5066008#0


#12
test = ['I','Like','Python','automation']

print ''.join(test)

#13
testList = [1,4,5]
testList.reverse()
print (testList)

for element in reversed([1,23,4,5]):
	print (element)

"xiaoniao"[::-1]

[1,2,4,9][::-1


#14
testlist = [10,20,30]
for index,value in enumerate(testlist):
	print (index,': ',value)
	
#15
class Shapes:
	Circle,Square,Triangle,Quadrangle = range(4)
	
print (Shapes.Circle)
print (Shapes.Square)
print (Shapes.Triangle)
print (Shapes.Quadrangle)

#16
def x():
	return 1,2,3,4
	
a,b,c,d = x()

#17

def test(x,y,z):
	print (x,y,z)

testDict = {'x':1,'y':2,'z':3}
testList = [10,20,30]

test(*testDict) #一个星号的时候只对键有作用

test(**testDict) #两个星号的时候只对作用

test(*testList) #如果是列表的话，解包只需要一个星号


#18
#使用字典来存储选择操作
stdcalc = {
	'sum':lambda x,y:x + y,
	'subtract':lambda x,y: x - y
	}

print (stdcalc['sum'](9,3))
pritn (stdcalc['subtract'](9.3))


#19
#python2
result = (lambda k :reduce(int.__mul__,range(1,k + 1),1))(3)
print (result)

#python3
import functools
result = (lambda k : functools.reduce(int.__mul__,range(1,k + 1),1))(3)

print (result) # 6


#20
#找到列表中出现最频繁的数

test = [1,2,3,4,2,2,3,1,4,4,4]
print (max(set(test),key = test.count))

#21
#重置递归限制
import sys
x = 1001
print (sys.getrecursionlimit())

sys.setrecursionlimit(x)
print (sys.getrecursionlimit())


#22
#检查一个对象的内存使用
#在python 2.7中，一个32比特的整数占用24字节，在python 3.5中利用28字节。为确定
#内存使用，我们可以调用getsizeof方法。

#在python 2.7 中：
import sys
x = 1
print (sys.getsizeof(x))
# ---> 24

#python 3.5 中：
import sys
x = 1
print (sys.getsizeof(x))
#----> 28

#23
#使用__slots__来减少内存开支
#你是否注意到你的python应用占用许多资源特别是内存，有一个技巧是使用__slots__类变#量来在一定程度上减少内存开支

import sys

class FileSystem(object):
	def __init__(self,files,folders,devices):
		self.files = files
		self.folders = folders
		self.devices = devices
print (sys.getsizeof(FileSystem))

class FileSystem_1(object):
	__slots__ = ['files','folders','devices']
	def __init__(self,files,folders,devices):
		self.files = files
		self.folders = folders
		self.devices = devices

print (sys.getsizeof(FileSystem_1))

#很明显，可以从结果中看到确实有内存使用上的节省，但是你只应该在一个类的内存开销
#不必要得大时才使用__slots__。只在对应用进行性能分析后才使用它，不然的话，你只是使得代码难以改变而没有真正的益处。
