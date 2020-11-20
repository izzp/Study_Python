"""
任务：给定一个密码字符串，判断该密码的安全性。如果密码符合低级要求则打印"低级密码"，
如果密码符合中级要求则打印"中级密码"，如果密码符合高级要求则打印"高级密码"，
"""
import string
password = input()     # 获取密码字符串

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 通过本章节所学的知识来判断密码的安全性
k=string.punctuation
p=0
P=0
P1=0
P2=0
for i in password:
    for j in k:
        if(i==j):
            p=1
L=string.ascii_letters
for i in L:
    if(password[0]==i):
        P=1
for i in password:
        if(i.isdigit()):
            P1=1
for i in password:
        if(i.isalpha()):
            P2=1
if(len(password)>=8 and p==1 and P2==1 and p==1 and P==1):
    print('高级密码')
elif(P1==1 and P2==1):
    print('中级密码')
else:
    print('低级密码')
########## End ##########
