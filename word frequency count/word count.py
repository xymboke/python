#对给定的英语文章进行单词频率统计，使用字典

#读取Txet文件
txt=open('hamlet.txt','r').read()
txt=txt.lower()
for ch in "~!@#$%^&*()`_+-=\|':;.,<>/?\"[]{}":
    txt=txt.replace(ch,' ') #用空格代替特殊符号
words=txt.split()#以空格分离字符串


#统计
counts={}
sumcount=0
for word in words:
    counts[word]=counts.get(word,0)+1
    sumcount=sumcount+1

print('单词总数为：',sumcount)
print('分别是：')
for key in counts.keys():
    print(key,counts[key])
    
