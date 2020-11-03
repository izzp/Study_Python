"""
任务：给定一个编码之后的字符串，请输出它的编码方式，并输出解码之后的字符串。结果以字典的形式输出。
输出格式：{"编码格式": "gbk","字符串":···}
"""
string = eval(input())

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 第一步：导入检测模块
import chardet
# 第二步：对字符串进行解码并按照要求输出结果
result1 = chardet.detect(string)
bianma = result1['encoding']
result2 = string.decode(encoding=bianma)
print("{'编码格式': '%s', '字符串': '%s'}"%(bianma,result2))
########## End ##########
