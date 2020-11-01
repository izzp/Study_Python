"""
任务：定义一个生成器函数 fib()，实现打印斐波拉契数列的前 n 项。n 是用过 input 获取。
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 定义生成器函数 fib()，实现斐波拉契数列的打印
def fib(n):
    f1 = 1
    f2 = 1
    if n == 1 or n == 2:
        yield 1
    else:
        for i in range(1, n - 1):
            f1, f2 = f2, (f1 + f2)
        yield f2


n = int(input())
for x in range(n):
    print(next(fib(x + 1)))
########## End ##########
