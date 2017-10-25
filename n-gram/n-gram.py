import re
from collections import Counter


#训练语料
file_in=open('E:\学习资料\研一上课件\计算机语言学\北大(人民日报)语料库199801.txt','r',encoding='UTF-8')
#测试数据集
file_testdata=open('./input.txt','r')
#输出结果
file_out=open('./2017110645.txt','w')

# input_str=input('输入要处理的字符串')
input_str=file_testdata.read()
file_testdata.close()

wordList=Counter()   #词库，key-词  val-频次

strlist=file_in.readlines()
for str in strlist:
    # 过滤空行
    str = str.strip()
    if not str:
        continue

    linelist=re.split(' +|\n',str)
    linelist=linelist[1:]  #去掉行首标签
    linelist=list(map(lambda w:w[:w.find('/',0)].strip(),linelist)) #去掉词尾的标记,并且去除首尾的空格
    wordList.update(linelist)

N=sum(wordList.values()) #词库总的大小
MaxLen=len(max(wordList.keys(),key=len))  #词的最大长度

#切分结果的数据结构['start','end','rate','rate_cal','law']
#start-end 分别指向的就是子串的起始和终止位置本身
START,END,RATE,RATE_CAL,LAW=0,1,2,3,4

word_pool=[]   #可能作为切分结果的字符串池
i,j=0,0
inputStrLen=len(input_str)
laplaceNum=0   #平滑的词计数

#找到所有可能的划分，并且写入rate（平滑的rate记作0）
while i<inputStrLen:
    j=i
    while j<inputStrLen and j-i<MaxLen:
        times=wordList.get(input_str[i:j+1])
        #j==i 表示的是单个字，即只将词库中的词以及单个字作为可能的切分结果
        #即：对于OOV不进行处理，OOV中的词以单字的形式进行切分
        #词库中存在的词

        #对于行首的词RATE_CAL都不等于-1，因为第一个词的RATE_CAL=rate
        if times:
            rate=times/N   #计算概率
            if i == 0:
                # 句首词，累加的概率等于词在词库中的概率
                word_cal = [i, j, rate, rate,-1]
            else:
                word_cal = [i, j, rate, -1,-1]
        #不在词库中的句首单字
        elif j==i and i==0:
            laplaceNum=laplaceNum+1
            # i=j=0且不再词库中的情形下，需要单独给出Rate的计算（laplace需要在扫描完之后才能得到值）
            word_cal = [i,j,0,0,-1]
        #不在词库中的非句首单字
        elif j==i:
            laplaceNum=laplaceNum+1
            word_cal=[i,j,0,-1,-1]
        word_pool.append(word_cal)
        j=j+1
    i=i+1
#平滑值
laplace=1/(N+laplaceNum)

#求rate_cal
for word in word_pool:
    if  word[RATE_CAL]==-1:
       candidate=list(filter(lambda x:x[END]==word[START]-1,word_pool))
       rate_cal_max=max(candidate,key=lambda w:w[RATE_CAL])
       #针对于i==j>0 且不在 词库中的词，平滑处理
       if word[RATE]==0:
           word[RATE]=laplaceNum
       word[RATE_CAL]=rate_cal_max[RATE_CAL]*word[RATE]
       word[LAW]=rate_cal_max[START]
    elif word[RATE_CAL]==0:
        word[RATE]=laplace
        word[RATE_CAL]=laplace

#结果集合，保存的内容是字符串
res_list=[]
end=inputStrLen-1

#查找最优的词尾
bestEndCandadaite=list(filter(lambda x:x[END]==end,word_pool))
bestEnd=max(bestEndCandadaite,key=lambda w:w[RATE_CAL])
res_list.append(input_str[bestEnd[START]:])

#向前查找位置
start=bestEnd[LAW]
end=bestEnd[START]
while start>=0:
    res_list.append(input_str[start:end])
    bestEnd=list(filter(lambda w:w[START]==start and w[END]==end-1,word_pool))[0]
    start = bestEnd[LAW]
    end = bestEnd[START]

#输出结果
for w in res_list[::-1]:
     file_out.write(w+' ')
    # print(w)
file_out.write('\n')

file_in.close()
file_out.close()
print('end')




































