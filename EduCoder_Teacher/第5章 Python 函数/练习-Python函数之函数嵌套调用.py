"""
任务：编写函数 count() 和 statistic()，statistic() 函数参数接收一个字符串，返回字符串中每个字符及该字符出现次数的一个字典，count() 函数用于计算每个字符在字符串中出现的次数。函数中需要用到的字符串通过 input() 获取。
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
##########Begin##########
# 定义count()函数
def statistic(s):
    dic={}
# 定义嵌套函数count()
    def count(ch1,s):
        num=0
        for x in s:
            if x==ch1:
                num+=1
        return num
    for i in s:
        if i not in dic:
            dic[i]=count(i,s)
        else:
            continue
    return dic

# 获取字符串，调用函数并输出结果字典
s=input()
print(statistic(s))

# 定义 statistic()函数

# 获取字符串，调用函数并输出结果字典
string = input()
print(statistic(string))

##########End##########
