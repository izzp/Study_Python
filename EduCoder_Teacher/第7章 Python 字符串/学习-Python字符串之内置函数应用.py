"""
任务：给定一个字符串，利用内置函数判断该字符串是否为回文串。该字符串通过 input 函数获取。如果是回文串则输出“是回文串”，如果不是则输出“不是回文串”。
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 利用内置函数判断该字符串是否为回文串
string1=list(input())
string2=reversed(string1)
list1=list(string1)
list2=list(string2)
i=0
flag=0
while i < len(list1):
    if list1[i]==list2[i]:
        i=i+1
    else:
        flag=1
        break
if flag==0:
    print('是回文串')
else:
    print('不是回文串')
########## End ##########


