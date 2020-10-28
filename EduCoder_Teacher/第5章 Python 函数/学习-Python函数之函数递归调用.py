"""
任务：使用递归打印斐波拉契数列的前 n 位数字。n 通过 input 函数获取。
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 定义一个函数，使用递归打印斐波拉契数列的前 n 位数字
def add(n):
    if n > 2:
        return (add(n - 1) + add(n - 2))
    if n == 2:
        return 1
    if n == 1:
        return 0

n = int(input())
print(add(n+1))

########## End ##########
