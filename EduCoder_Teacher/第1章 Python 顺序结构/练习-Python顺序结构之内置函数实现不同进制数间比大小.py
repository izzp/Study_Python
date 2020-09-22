"""
任务：使用 max 函数得到两个数中的较大者并输出，这两个数通过 input 获取，第一个为二进制数，第二个为十六进制数。
"""
 
#请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
##########Begin##########
# 使用 max 函数得到两个数中的较大者并输出
num2=input()
num16=input()
num2=int(num2,2)
num16=int(num16,16)
m=max(num2,num16)
print(m)
##########End##########