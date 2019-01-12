#函数的参数
#概念 
"""
	位置参数
	默认参数
	可变参数
	关键字参数
	命名关键字参数
	参数组合
"""	  
def power(x):
	return x*x

print(power(5))

def power(x,n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print(power(2,5))
print(power(2))
#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，
#演示如下：
#先定义一个函数，传入一个list，添加一个END再返回：

def add_end(L = []):
	L.append('END')
	return L

print(add_end())
print(add_end())
print(add_end())
"""
原因解释如下：

Python函数在定义的时候，默认参数L的值就被计算出来了，
即[]，因为默认参数L也是一个变量，它指向对象[]，每次
调用该函数，如果改变了L的内容，则下次调用时，默认参
数的内容就变了，不再是函数定义时的[]了。
"""
#定义默认参数要牢记一点：默认参数必须指向不变对象！
#要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L = None):
	if L is None:
		L = []
	L.append('END')
	return L	
print(add_end())
print(add_end())
print(add_end())

#可变参数
#定义可变参数和定义一个list或tuple参数相比，
#仅仅在参数前面加了一个*号。在函数内部，参数
#numbers接收到的是一个tuple，因此，函数代码完
#全不变。但是，调用该函数时，可以传入任意个参数，
#包括0个参数：
def cals(*numbers):
	sum = 0
	for x in numbers:
		sum = sum + x
	return sum

print(cals(12,13))
print(cals(1,2,3,4))
#也可以用下面的写法

num = [1,2,3]

print(cals(*num))
# 关键字参数
"""
	可变参数允许你传入0个或任意个参数，
	这些可变参数在函数调用时自动组装为
	一个tuple。而关键字参数允许你传入0
	个或任意个含参数名的参数，这些关键
	字参数在函数内部自动组装为一个dict
"""
def person(name ,age ,**kw):
	print('name:',name,'age:',age,'other:',kw)

person('tjk',20)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
"""
关键字参数有什么用？它可以扩展函数的功能。
比如，在person函数里，我们保证能接收到name和age这两个参数，
但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正
在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都
是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
"""
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

#也可以简写
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

'''
	**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
	kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到
	函数外的extra
'''
#命名关键字参数

#对于关键字参数，函数调用者可以传入任意不受限制的关键字参数。至于到底传入那些，
#需要在函数内部对 kw 经行检查

#仍以person()函数为例，我们希望检查是否有city和job参数：

def person(name , age, **kw):
	if 'city' in kw:
		#有 city 参数
		pass
	if 'job'  in kw:
		pass
	print('name',name,'age',age,'other',kw)

person('Jack', 24, city='Beijing', addr='Chaoyang',zipcode = 123456)

#如果要限制关键字参数的名字，就可以用命名关键字参数，
#例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，
#  *后面的参数被视为命名关键字参数。
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
def person(name,age,*,city,job):
	print(name,age,city,job)
person('Jack', 24, city='Beijing', job='Engineer')


#  参数组合
"""
	在Python中定义函数，可以用必选参数、默认参数、可变参数、
	关键字参数和命名关键字参数，这5种参数都可以组合使用。但
	是请注意，参数定义的顺序必须是：必选参数、默认参数、可变
	参数、命名关键字参数和关键字参数。
    
    所以，对于任意函数，都可以通过类似func(*args, **kw)的形式
    调用它，无论它的参数是如何定义的。

	虽然可以组合多达5种参数，但不要同时使用太多的组合，否则
	函数接口的可理解性很差。
"""

#测试
#在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False ，
#即： not None == not False == not '' == not 0 == not [] == not {} == not ()
def product(*num):
	if not num:
		raise TypeError
	s = 1
	for x in num:
		s = s * x
	return s
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')	