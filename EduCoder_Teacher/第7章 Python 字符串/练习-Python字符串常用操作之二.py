"""
任务：给定一个字符串，判断该字符串是否是回文串。字符串通过 input 获取，如果是，则输出“是回文串”,如果不是，则输出“不是回文串”。
"""

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用字符串函数来判断字符串是否为回文串
s = input()
if not s:
    print('请不要输入空字符串！')
    s = input('请重新输入一个字符串：')
a = len(s)
i = 0
count = 1
while i <= (a/2):
    if s[i] == s[a-i-1]:
        count = 1
        i += 1
    else:
        count = 0
        break
if count == 1:
    print('是回文串')
else:
    print('不是回文串')
########## End ##########
