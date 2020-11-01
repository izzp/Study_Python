"""
任务：自定义函数message，实现学生的信息输出。
"""

'''
定义函数message，参数有位置参数name，默认参数age（默认值为6），可变参数scores,
关键字参数kw
'''


########### Begin ###########
# 第一步：定义参数
def message(name, age="6", *scores, **kw):
# 第二步：对可变参数scores进行求和，将结果赋值给result
    result=0
    for n in scores:
        result = result + n
# 第三步：通过print打印信息，输出格式可以参考下方的测试集
    print('name:', name, 'age:', age, 'result:', result, 'kw:',kw)
########### End ###########

# 以下为测试代码，不是本实训要求掌握的内容，请不要修改
if __name__ == '__main__':
    sign = int(input())
    if sign == 0:
        name = input()
        message(name)

    elif sign == 1:
        name = input()
        age = input()
        message(name, age=age)

    elif sign == 2:
        name = input()
        age = input()
        score1 = int(input())
        score2 = int(input())
        message(name, age, score1, score2)

    elif sign == 3:
        name = input()
        age = input()
        score1 = int(input())
        score2 = int(input())
        kw = {'hobby': 'basketball'}
        message(name, age, score1, score2, **kw)

    else:
        name = input()
        age = input()
        score1 = int(input())
        score2 = int(input())
        kw = {'height': 122, 'weight': 20}
        message(name, age, score1, score2, **kw)
