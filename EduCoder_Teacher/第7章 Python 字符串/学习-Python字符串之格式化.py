"""
任务：给定一个列表，计算列表内所有数据标准差，结果保留小数点后 2 位。
"""
import math

list1 = eval(input())
# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 计算列表内所有元素的标准差
num = 0  #和
s2 = 0
for x in list1:
    num += x
for y in list1:
    s2 += (y-num/len(list1))**2
result = math.sqrt(s2/len(list1))
# 使用格式化输出打印结果，并保留小数点后2位
print("%.2f" % result)
########## End ##########
