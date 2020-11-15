"""
任务：给定一个字母，判断字母的大小写，如果是大写，将该字母转换为小写，反之，将字母改为大写。
该字母通过 input 函数获取。打印转换后的字母。如果不是字母则输出“不是字母”
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用字符串函数实现字母大小写的切换
str = input()
if str.isupper():
    print(str.lower())
elif str.islower():
    print(str.upper())
else:
    print("不是字母")
########## End ##########
