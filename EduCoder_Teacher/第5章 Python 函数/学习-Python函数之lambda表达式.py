"""
任务：给定两个列表，编写一个匿名函数实现比较两个列表中对应下标位置的元素的大小，将大的元素组成一个新的列表，函数参数通过 input 获取。
"""

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 请使用map函数和lambda表达式实现本关任务
list1=eval(input())
list2=eval(input())
d=map(lambda x,y: x if x > y else y,list1,list2)
print(list(d))
########## End ##########
