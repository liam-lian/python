# 平滑方法：Laplace Smoothing 和 Interpolation 两种平滑一起使用

import re
from collections import Counter

wordList=Counter()   #词库，key-词  val-频次
file_in=open('E:\学习资料\研一上课件\计算机语言学\北大(人民日报)语料库199801.txt','r',encoding='UTF-8')
file_out=open('./2017110645.txt','w')

strlist=file_in.readlines()
for str in strlist:
    # 过滤空行
    str = str.strip()
    if not str:
        continue

    linelist=re.split(' +|\n',str)
    #去掉行首标签
    linelist=linelist[1:]
    #去掉词尾的标记
    linelist=list(map(lambda w:w[:w.find('/',0)],linelist))
    wordList.update(linelist)

N=sum(wordList.values()) #词库总的大小
MaxLen=len(max(wordList.keys(),key=len))  #词的最大长度

#切分结果的数据结构['start','end','rate','rate_cal','law']
#start-end 分别指向的就是子串的起始和终止位置本身
START,END,RATE,RATE_CAL,LAW=0,1,2,3,4

input_str=input('输入要处理的字符串')

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
        if times or j==i:
            #词库中存在的词
            if(times):
                rate=times/N   #计算概率
                if i == 0:
                    word_cal = [i, j, rate, rate,-1]   #句首词，累加的概率等于词在词库中的概率
                else:
                    word_cal = [i, j, rate, -1,-1]
            #不在词库中的句首单字
            elif i==0:
                laplaceNum=laplaceNum+1
                # i=j=0且不再词库中的情形下，需要单独给出Rate的计算（laplace需要在扫描完之后才能得到值）
                word_cal = [i,j,0,0,-1]
            #不在词库中的非句首单字
            else:
                laplaceNum=laplaceNum+1
                word_cal=[i,j,0,-1,-1]
            word_pool.append(word_cal)
        j=j+1
    i=i+1

laplace=1/(N+laplaceNum)
#求rate_cal
for word in word_pool:
    if  word[RATE_CAL]==-1:
       candidate=list(filter(lambda x:x[END]==word[START]-1,word_pool))
       rate_cal_max=max(candidate,key=lambda x:x[RATE_CAL])
       if word[RATE]==0:
           word[RATE]=laplaceNum
       word[RATE_CAL]=rate_cal_max[RATE_CAL]*word[RATE]
       if word[RATE_CAL]==0:
            print(word)
       word[LAW]=rate_cal_max[START]
    elif word[RATE_CAL]==0:
        word[RATE]=laplace
        if word[START]==0:
            word[RATE_CAL]=laplace

#结果集合，保存的内容是字符串
res_list=[]
end=inputStrLen-1
bestEndCandadaite=list(filter(lambda x:x[END]==end,word_pool))
bestEnd=max(bestEndCandadaite,key=lambda x:x[RATE_CAL])
res_list.append(input_str[bestEnd[START]:])

print('zzzzzz')
start=bestEnd[LAW]
end=bestEnd[START]
while start>=0:
    res_list.append(input_str[start:end])
    bestEnd=list(filter(lambda x:x[START]==start and x[END]==end-1,word_pool))[0]
    start = bestEnd[LAW]
    print(start)
    end = bestEnd[START]


for i in res_list[::-1]:
    # file_out.write(i+' ')
    print(i+' ')

file_in.close()
file_out.close()









#生命的风景






































