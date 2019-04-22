# -*- coding:UTF-8 -*-

"""
	函数
"""
"""

定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。


Python内置了很多有用的函数，我们可以直接调用。

要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：

http://docs.python.org/3/library/functions.html#abs

也可以在交互式命令行通过help(abs)查看abs函数的帮助信息
"""
"""
 自定义函数

	 在Python中，定义一个函数要使用def语句，
	 依次写出函数名、括号、括号中的参数和冒号:，
	 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
"""
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
print(my_abs(-90))