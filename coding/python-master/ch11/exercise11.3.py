#＃这个问题的基本概要是读取文件，使用refindall查找整数

#looking为[0-9] +的正则表达式，然后转换提取的字符串

#to整数并总结整数。

import re

hand = open('regex_sum_297209.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) > 0:
        for i in x:
            print(i)
            num = float(i)
            numlist.append(num)

print(sum(numlist))
