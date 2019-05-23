str1='爱 上 了 的 积 分 >>> www.mingrisoft.com'
print('原字符串: ',str1)
list1= str1.split()  #采用默认分隔符进行分割
list2=str1.split('>>>') #采用多个字符进行分割
list3= str1.split('.') #采用.号进行分割
list4= str1.split(' ',4) #采用空格进行分割，并且只分割前4个
print(str(list1) + '\n' + str(list2) + '\n' + str(list3) +'\n'+ str(list4))
list5= str1.split('>')  #采用>进行分割
print(list5)

print('='*40)


str6= '@圣诞节快乐放假 @都结束了卡减肥 @时间到了发空间啊'
list6 = str6.split(' ')  #用空格分割字符串
print('您@的事有：')
for item in list6:
    print(item[1:])  #输出每个好友时，去掉@符号


print('*='*40)
list_friend=['案件司法局','安吉拉开始','案件是否','阿莎','阿莎奋斗'] #列表
str_friend= '@'.join(list_friend)  #用空格+@符号进行连接
at='@'+str_friend  #由于使用join()方法时，第一个元素前不加分隔符，所以需要在前面加上@符号
print('您要@的好友: ',at)
