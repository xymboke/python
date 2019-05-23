mot_en='Remembrance is a form of meeting. Forgetfulness is a form of freedom.'
mot_cn='记忆是一种相遇。遗忘是一种自由。'
print(mot_en + '--'  + mot_cn)


'''
str1='我今天一共走了'  #定义一个字符串
num=12098   #定义一个整数
str2='步'   #定义字符串
print(str1 + num + str2)  #对字符串和整数进行拼接
'''

str1='我今天一共走了'  #定义一个字符串
num=12098   #定义一个整数
str2='步'   #定义字符串
print(str1 + str(num) + str2)  #对字符串和整数进行拼接


programmer_1='程序员甲：搞IT太辛苦了，我想换行....怎么办？'
programmer_2='程序员乙：敲一下回车键'
print(programmer_1 + '\n' + programmer_2)

str1='人生苦短，我用python!'  #定义字符串
length = len(str1)  #计算字符串的长度
print(length)

str1='人生苦短，我用python!'  #定义字符串
length = len(str1.encode())  #计算utf-8编码字符串的长度
print(length)


str1='人生苦短，我用python!'  #定义字符串
length = len(str1.encode('gbk'))  #计算GBK编码字符串的长度
print(length)
