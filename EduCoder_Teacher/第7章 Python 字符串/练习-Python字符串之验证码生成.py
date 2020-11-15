"""
任务：请编写代码实现生成一个 n 位的验证码，验证码可由大小写字母和数字组成。
"""
import string
import random
n = int(input())     # 验证码的位数

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用string和random模块随机生成n位的验证码，将生成的验证码赋值给变量 result
str1=string.ascii_letters+string.digits
result=""
for i in range(n):
    result=result+random.choice(list(str1))
########## End ##########
if result.isalnum() and len(result)==n:
	print(result)
	print("验证码生成成功")
else:
	print("验证码生成错误")