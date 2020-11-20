"""
任务：给定一个字符串，该字符串中包含了许多邮箱号，使用字符串函数筛选出这些邮箱号，并根据不同的电子邮件服务商来分类。
分类结果为一个字典，字典的键为邮箱号中`@`和`.com`之间的一截，字典的值为包含邮箱号的列表。
"""
str1 = input()     # 包含邮箱号的字符串
# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用字符串函数筛选出这些邮箱号，并根据不同的电子邮件服务商来分类
str2 = str1.split(",")
str3 = []
result = []
for i in str2:
    k = i.split("@")[1].split(".")[0]
    str3.append(k)
str3 = sorted(list(set(str3)))
for x in str3:
    list2 = []
    for y in str2:  # 遍历所有邮箱
        if (x == y.split("@")[1].split(".")[0]):
            list2.append(y)  ## 如果是x的服务商
    result.append(x + ":" + ",".join(list2))
print(result)
########## End ##########
