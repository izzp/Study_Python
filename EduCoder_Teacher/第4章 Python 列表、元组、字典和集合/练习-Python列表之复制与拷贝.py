import copy


list1 = eval(input())     # 获取列表

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用所学的拷贝来完成本关任务，打印删除指定元素后的列表
list1=list(filter(lambda s:isinstance(s,int)==True or len(s)<=3,list1))
print(list1)
########## End ##########
