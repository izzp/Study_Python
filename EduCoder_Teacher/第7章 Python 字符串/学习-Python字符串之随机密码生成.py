"""
任务：编写代码实现随机生成一个 8 位数的密码。
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用 random 模块实现随机生成一个 8 位数的密码，将密码赋值给变量 password
import random
password = random.randint(10000000,99999999)
########## End ##########
if len(str(password)) == 8:
    print(password)
    print("随机密码生成成功")
else:
    print("随机密码生成失败，长度不为8")