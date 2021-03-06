"""
任务：给定一个整数 n，判断 n 以内的正数是否含有水仙花数，n 通过 input 获取;
如果有，输出“有水仙花数”，如果没有，则输出“没有水仙花数”。
"""

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用for-else判断 n 以内的正数是否含有水仙花数
n = int(input())
for n in range(100,n+1):
    g = n % 10
    s = n // 10 % 10
    b = n // 100
    if g ** 3 + s ** 3 +b ** 3 == n:
        print("有水仙花数")
        break
else:
    print("没有水仙花数")
########## End ##########
