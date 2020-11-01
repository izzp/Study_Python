"""
任务：使用作用域中相关的关键字修改下列 begin-end 中的代码，使函数 average 实现计算平均分的功能。
"""

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
##########Begin##########
# 请使用作用域相关的关键字修改下列代码，实现计算平均分的功能
def average(*args):
    def sum(args):
        global score
        score  = 0
        for x in args:
            score += x
    sum(args)
    return score / len(args)
##########End##########
result = average(56,76,84,98,78,79,89,67,86,78,67,67,95,24,96,96,86,65,83,86,80)
print(result)