"""
任务：创建一个函数 Number，函数的功能为判断一个整数是否为正数，如果是正数，返回 True，如果是不是正数，
返回 False。被判断的整数都是通过 input 获取。如果是正数，打印"是正数"，如果不是正数，打印"不是正数"。
"""

num = int(input())     # 被判断的整数
# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
##########Begin##########
# 第一步：创建一个函数 Number，函数的功能为判断数字是否是正数，如果是正数，返回 True，如果是负数，返回 False
def Number(num):
    if num>0:
        return "True"
    else:
        return "False"
# 第二步：判断函数的返回值，按照任务要求打印信息
if Number(num)=="True":
    print("是正数")
else:
    print("不是正数")
##########End##########
