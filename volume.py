"""
任务：使用 math 模块的数学函数来计算半径为 R 的球体的体积，R 使用 input 函数获取，数据类型为整型。
"""
# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########### Begin ###########
# 第1步：导入math模块
import math
# 第2步：使用input函数获取球体的半径赋值给R
R=float(input())
# 第3步：计算球体的体积，将结果赋值给result
result=4/3*math.pi*R*R*R
# 第4步：打印出球体的体积，结果四舍五入后保留 5 位小数
print("%.5f" % result)
########### End ##########
