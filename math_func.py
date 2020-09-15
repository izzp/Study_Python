"""程序代码
任务：已知直角三角形的斜边计算公式，其中邻边 x 和 y 我们通过键盘输入获取，且都为整型。请使用 math 库中的函数来求斜边 d 的值。
"""

#请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########### Begin ###########
# 第1步：导入Python中的模块math
import math
# 第2步：使用input获取输入值赋值给x
x=int(input())
# 第3步：使用input获取输入值赋值给y
y=int(input())
# 第4步：使用math中的数学函数计算斜边长，将结果赋值给d
d=math.sqrt(x*x+y*y)
# 第5步：打印出斜边长的值
print(d)
########### End ###########
