# -*-Coding: UTF-8 -*-


"""
   三 、进阶数据类型
"""

'''
   list 列表, tuple 元组, dict 字典, set。 
'''
"""
	1、list
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




