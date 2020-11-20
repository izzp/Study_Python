"""
任务：输出如下所示格式美观的杨辉三角的前 n 行。n 通过 input 函数获取。下例为 n=7 时的杨辉三角。具体输出情况可以查看预期输出。
```
                  1
               1     1
            1     2     1
         1     3     3     1
      1     4     6     4     1
   1     5    10    10     5     1
1     6    15    20    15     6     1
```
"""

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用字符串格式化输出方式打印杨辉三角
n = int(input())
s = [[1]]
for i in range(n):
    t = []
    for j in range(len(s[i])):
        if j == 0:
            t.append(1)
        else:
            t.append(s[i][j - 1] + s[i][j])
    t.append(1)
    s.append(t)

k = 3*n+1
for i in range(n):
    print(' '*k, end = '')
    for j in range(len(s[i])):
        if j == 0:
            print(str(s[i][j]), end = '')
        else:
            print('%6d'%(s[i][j]), end = '')
    print(' ' *k)
    k -= 3

########## End ##########
