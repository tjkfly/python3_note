# -*- coding:UTF-8 -*-

"""
	条件判断
	语法就规定了缩进
    注意冒号 ：
	else if 要写成 elif 
"""
age = 20
if age >= 18:
	print("man")
else:
	print("child")

"""
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
"""
birth = input('birth: ')
birth = int(birth)            # 用int() 把str转换为int型
if birth < 2000:
    print('00前')
else:
    print('00后')

"""
   循环
"""    
sum = 0
for x in [1,2,3,4,5]:
    sum = sum + x
print(sum)
"""
    如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，
    再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
"""
"""
第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
比如我们要计算100以内所有奇数之和，可以用while循环实现：
   break  continue
"""
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)    