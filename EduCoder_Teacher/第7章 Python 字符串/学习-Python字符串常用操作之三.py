# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用字符串函数来判断电话号码的运营商
number = input()
if number.startswith("130"):
    print("中国联通")
elif number.startswith("133"):
    print("中国电信")
elif number.startswith("134"):
    print("中国移动")
else:
    print("输入数据不合法")
########## End ##########
