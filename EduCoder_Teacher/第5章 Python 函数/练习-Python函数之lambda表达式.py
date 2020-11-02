"""
任务：将下列函数转换为匿名函数，该函数的作用是得到列表中的偶数，函数参数通过 input 获取。
将列表中的偶数添加到一个新列表中，打印纯偶数的列表。
```
def func(num_list):
	list1 = []
	for x in num_list:
		if x%2 == 0:
			list1.append(x)
	return list1
```
"""


# 请在下面的 Begin-End 之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 请使用 lambda 表达式实现本关任务
list1=eval(input())
list2=list(filter(lambda x:x%2==0,list1))
print(list2)
########## End ##########
