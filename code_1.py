# -*- coding: UTF-8 -*-


"""
    先学习注释方法
    1、#  单行注释
    2、''' '''  三对单引号注释
    3、或者三对双引号
"""


"""
  print() 输出
  相当灵活的输出用法
"""
# 1、打印字符
print('hello,word')
# print()会依次打印每个字符串，遇到逗号“,”会输出一个空格，因此，输出的字符串是这样拼起来的：
print('hello','word')


# 2、打印整数,计算结果
print(521,'Python')
print(123 + 230)
res = 123 + 234
print(res)

"""
   格式化输出 
   与c语言一致
"""
print('%s is %d years old,get %.2fpoints'%('tjk',20,99.90))




"""
	input 输入  	
"""
name = input()
print(name)
name = input('please input ')
print(name)



"""
可以没有输入，但是一定要有输出。
太灵活，有时也会让人手无足措！！！
"""