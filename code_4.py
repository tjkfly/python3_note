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