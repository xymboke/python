programer_1='你知道我的生日吗？' #程序员甲问程序员乙的台词
print('程序员甲说：',programer_1)
programer_2='阿斯蒂芬水电费'
print('程序员乙说：',programer_2)

idcard = '2132545335454564654546545'
print('程序员甲说:',idcard)

birthday = idcard[6:10] + '年' + idcard[10:12] +  '月' + idcard[12:14] + '日'
print('程序员乙说:','你是' + birthday + '出生的，所以你的生日是' + birthday[5:])
