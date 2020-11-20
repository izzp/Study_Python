"""
任务：给定一个字符串，统计字符串中每个字符在该字符串中出现位置的所有下标。输出一个字典，字典的键为字符，值为该字符出现的所有下标。
举个例子：“hello”   输出结果：{"h":[0],"e":[1],"l":[2,3],"o":[4]}
"""

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用字符串函数完成本关任务，并按照要求打印结果
str1 = input()

dict1 = {}
for x in list(str1):
    index_num = []
    num = 0
    while True:
        num = str1.find(x,num)
        if num == -1:
            break
        index_num.append(num)
        num += 1
    dict1[x] = index_num

print(dict1)
########## End ##########
