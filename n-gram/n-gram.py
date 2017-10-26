import re
from collections import Counter
import sys

if len(sys.argv) < 3:
    sys.exit('ERROR 命令行参数依次为：训练语料文件、测试语料文件');

# # 训练语料
# file_in = open('E:\学习资料\研一上课件\计算机语言学\北大(人民日报)语料库199801.txt', 'r', encoding='UTF-8')
# # 测试数据集
# file_testdata = open('./input.txt', 'r')
# # 输出结果
# file_out = open('./2017110645.txt', 'w')
try:
    # 训练语料
    file_in = open(sys.argv[1], 'r', encoding='UTF-8')
    # 测试数据集
    file_testdata = open(sys.argv[2], 'r')
    # 输出结果
    file_out = open('./2017110645.txt', 'w')
except IOError as e:
    sys.exit(e);

# input_str=input('输入要处理的字符串')
input_str = file_testdata.read()
file_testdata.close()

wordList = Counter()  # 词库，key-词  val-频次

strlist = file_in.readlines()
for strLine in strlist:
    # 过滤空行
    strLine = strLine.strip()
    if not strLine:
        continue
    linelist = re.split(' +|\n', strLine)
    linelist = linelist[1:]  # 去掉行首标签
    linelist = list(map(lambda x: x[:x.find('/', 0)].strip(), linelist))  # 去掉词尾的标记,并且去除首尾的空格
    wordList.update(linelist)

inputStrLen = len(input_str)

i, j = 0, 0
# 计算平滑值，实现策略是，对于在词库中的词直接加入待拆解pool,除此之外之外只有单字可以入池
# 即：对于OOV不进行处理，OOV中的词以单字的形式进行切分。因此预处理，直接考察所有的单字，加入词库中，有利于计算平滑值
# 如果需要平滑，则将词库中所有的词的频次加1
laplaceList = []
while i < inputStrLen:
    if not wordList.get(input_str[i]):
        laplaceList.append(input_str[i])
    i = i + 1
if len(laplaceList):
    wordList.update(wordList.keys())
    wordList.update(laplaceList)

N = sum(wordList.values())  # 词库总的大小
MaxLen = len(max(wordList.keys(), key=len))  # 词的最大长度

# 切分结果的数据结构[START, END, RATE, RATE_CAL, LAW ]
# START, END 分别指向的就是子串的起始和终止位置本身
START, END, RATE, RATE_CAL, LAW = 0, 1, 2, 3, 4

word_pool = []  # 可能作为切分结果的字符串池
word_cal = []  # 存放单个的切分数据

i, j = 0, 0
# 找到所有可能的划分，并且写入rate
while i < inputStrLen:
    j = i
    while j < inputStrLen and j - i < MaxLen:
        times = wordList.get(input_str[i:j + 1])
        if times:
            rate = times / N  # 计算概率
            if i == 0:
                # 句首词，累加的概率等于词在词库中的概率
                word_cal = [i, j, rate, rate, -1]
            else:
                word_cal = [i, j, rate, -1, -1]
        word_pool.append(word_cal)
        j = j + 1
    i = i + 1

# 求rate_cal
for word in word_pool:
    if word[RATE_CAL] == -1:
        candidate = list(filter(lambda x: x[END] == word[START] - 1, word_pool))
        rate_cal_max = max(candidate, key=lambda x: x[RATE_CAL])
        word[RATE_CAL] = rate_cal_max[RATE_CAL] * word[RATE]
        word[LAW] = rate_cal_max[START]

# 结果集合，保存的内容是字符串
res_list = []

# 查找最优的词尾
bestEndCandadaite = list(filter(lambda x: x[END] == inputStrLen - 1, word_pool))
bestEnd = max(bestEndCandadaite, key=lambda x: x[RATE_CAL])
res_list.append(input_str[bestEnd[START]:])

# 向前查找位置
start = bestEnd[LAW]
end = bestEnd[START]
while start >= 0:
    res_list.append(input_str[start:end])
    bestEnd = list(filter(lambda x: x[START] == start and x[END] == end - 1, word_pool))[0]
    start = bestEnd[LAW]
    end = bestEnd[START]

# 输出结果
for w in res_list[::-1]:
    file_out.write(w + ' ')
    # print(w)
file_out.write('\n')

file_in.close()
file_out.close()
print('end')
