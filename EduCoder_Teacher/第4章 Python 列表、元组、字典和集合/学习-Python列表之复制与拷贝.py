# 请在下面的 Begin-End 之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 第1步：使用 input 函数获取列表
x=eval(input())
# 第2步：去除列表内的非重复值，打印处理后的列表
y=[]
for i in x:
    if x.count(i)!=1:
        y.append(i)
print(y)
########## End ##########
