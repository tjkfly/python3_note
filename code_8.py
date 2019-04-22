"""
   切片（Slice）

"""
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
 #取前3个元素，应该怎么做？
r1 = [L[0], L[1], L[2]]

r2 = []
n = 3
for i in range(n):
	r2.append(L[i])

print(r1,r2)	
"""
   使用切片
"""
r3 = L[0:3]  #或者L[:3]
print(r3)
def trim(s):
	while s[:1] == ' ':
	    s=s[1:]
	while s[-1:] == ' ':
	    s=s[:-1]
	return s

# 测试:
if trim('    hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
"""
	迭代
	如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

在Python中，迭代是通过for ... in来完成的


Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
"""
d = {'a':1,'b':2,'c':3}
for key in d:
	print(key)