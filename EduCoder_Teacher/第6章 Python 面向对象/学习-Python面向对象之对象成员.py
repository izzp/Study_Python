"""
任务：请修改右侧 Begin-End 之间的代码，使其可以正常运行。该代码的目的是求输入数据的阶乘。
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
class Factorial:
	def __init__(self,num):
		self.num = num
	def get_value(self):
		x = 1
		for i in range(1, self.num + 1):
			x = x * i
		return x

num = int(input())
f = Factorial(num)
print("%d的阶乘为%d"%(f.num,f.get_value()))
########## End ##########
