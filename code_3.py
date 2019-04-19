# -*-Coding: UTF-8 -*-


"""
   三 、进阶数据类型
"""

'''
   list 列表, tuple 元组, dict 字典, set。 
'''
"""
	1、list   用方括号
	   (1)有序集合，可以随其添加和删除元素
	   (2)len()函数 可以获取list元素的个数
	   (3)用索引来访问每一个位置的元素,从0 开始
	   (4)元素的数据类型可以不同
       (5)可以倒序访问 从 -1 推
       (6)大小可变，append 末尾添加，pop 末尾删除
          pop(i),删除指定位置i处的元素
          insert(i,x)指定位置i 插入元素x, 
       (7)list的元素可以是list 可以使用类似高维数组的形式访问  
"""
friends = ['Mic','Bob','li']
print(friends,len(friends))
friends.append('jk')
print(friends,len(friends))
friends.pop()
print(friends,len(friends))

girl = ['l1','l2','l3']
friends.insert(2,girl)
print(friends,len(friends))
print(friends[2][0],friends[2][1],friends[2][2])

"""
	tuple      用圆括号 
	元组  与list 相似，一旦初始化就不可修改 ,没有append 和 insert的方法
"""
friend = ('lili','joh','siri')
print(friend)

'''
   tuple 一旦定义不可修改，可以定义空的tuple
'''
t = ()
print(t)
'''
   t=(1)   这是个坑  ---> t = (1,)
'''
t = (1)
t1 = (1,0)
print(t,t1)
print('%s is %d'%(t1[0],t))

"""
	dict (dictionary) 字典  键值对。查找速度快
	就剩花括号了(哈哈)


	为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。
假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一
页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的
方法，list越大，查找越慢。

	第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，
然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不
会随着字典大小的增加而变慢。

	dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就
可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内
存地址，直接取出来，所以速度非常快。
"""
d = {'tjk':99,'bob':89,'rm':20}
print(d['tjk'])

d['rm'] = 19

print(d)

"""
	1、由于一个key只能对应一个value，所以，多次对一个key放入value，
后面的值会把前面的值覆盖：
    2、key不存在就会报错，可以通过两种方式避免
    (1)、in   返回bool值
    (2)、get()
"""
x = 'tj' in d
print(x)

d['ffaf'] = 888
print(d)
"""
 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：


"""



'''
	set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合：	
'''

#重复元素在set中自动被过滤：
s = set([1,2,3,2,3,4,4,1])
print(s)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(34)
print(s)
#通过remove(key)方法可以删除元素：
s.remove(34)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
tuple1 = (1,2,3)
s.add(tuple1)
print(s)