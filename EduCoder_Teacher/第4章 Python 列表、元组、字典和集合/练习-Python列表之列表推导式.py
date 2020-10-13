"""
任务：给定一个列表，使用列表推导式找出列表中长度大于 5 的名字，并打印该列表。
"""
 
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
 
# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
##########Begin##########
# 使用列表推导式找出列表中长度大于 5 的名字，并打印该列表
names2=[num for elem in names for num in elem]
names3 = [i for i in names2 if len(i)>5 ]
print(names3)

##########End##########
