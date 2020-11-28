class Account:
# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 第1步：补充实例属性
    def __init__(self,username,password):
        self.account_list = {}     # 用于存储传入的账号名和密码
        self.username=username
        self._password=password
# 第2步：定义账号添加函数add，将账号添加至account_list
    def add(self):
        self.account_list[self.username] = self._password
# 第3步：定义账号查询函数select，返回账号名
    def select(self):
        return ",".join(list(self.account_list.keys()))
########## End ##########
username = input()     # 账号名
password = input()     # 密码
a = Account(username,password)
a.add()
print("添加成功")
name = a.select()
print("账号名为：%s"%name)