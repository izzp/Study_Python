"""
任务：分别统计给定的列表中奇数和偶数的个数。
"""

list_value = [1, 2, 18, 7, 33, 22, 1045, 98, 78, 36, 10, 111, 105, 4320, 1014, 50, 63, 15, 18, 910, 2010, 3201, 2501, 25, 120, 320]

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
##########Begin##########
# 使用for循环统计给定的列表中奇数和偶数的个数，并按照输出格式打印出结果
j=0
o=0
for i in list_value:
    if i % 2 == 0:
        o += 1
    else:
        j += 1
print("奇数共%d个，偶数共%d个"%(j,o))
##########End##########
