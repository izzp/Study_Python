"""
任务：定义一个函数 average，用于计算考试成绩的平均分，每次传入的参数个数不确定，如果参数中出现了小于 0 或者大于 100 的数时，输出"分数数据异常"，否则输出平均分。
"""

 
# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
##########Begin##########
# 定义函数 average，计算平均分并按照要求返回结果
def average(*list):
	sumscore = 0
	for x in list:
		if x > 100 or x < 0:
			return 0
		sumscore += x
	return sumscore / len(list)

##########End##########
# 请勿修改下列代码
score = eval(input())     # 将输入的字符串转换为可执行的表达式
if score:
	print("平均分为",score)
else:
	print("分数数据异常")