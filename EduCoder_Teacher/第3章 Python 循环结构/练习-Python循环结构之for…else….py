"""
任务：给定一个正整数 n，这个正整数通过 input 获取，统计 2 到 n 的素数个数是否超过了 10 个。
如果超过了 10 个，则输出“素数数量超过10个”，如果少于 10 个，则输出“素数数量少于10个”，如果输入的数是 0 或 1，则输出“输入数据不合法”。
"""

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
##########Begin##########
# 使用input获取正整数n，判断2到n的素数是否超过十个
n = int(input())
add = 0
if n == 0 or n == 1:
    print("输入数据不合法")
else:
    for num in range(2, n+1):
        if num == 2:
            add += 1
        else:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                add += 1
    if add > 10:
        print("素数数量超过10个")
    else:
        print("素数数量少于10个")

##########End##########
