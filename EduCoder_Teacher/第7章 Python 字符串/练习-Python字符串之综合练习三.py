"""
任务：给定一个字符串，该字符串是一个包含地名、空格、特殊符号和 html 标签的字符串，请使用字符串函数筛选出其中的地名。
"""

str1 = input()

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用字符串函数来清洗出字符串中的地名
str2 = str1.strip().replace("<p>","").replace("</p>","").replace("<div>","").replace("</div>","")
result = "".join(str2.split("**"))
print(result)
########## End ##########