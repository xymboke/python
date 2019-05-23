print("2017到2018赛季NBA西部联盟前八名：")
team = ["按罚款 打开","打蜡 安抚","高傲的 安抚啊","爱啊符 如果","截个屏 同花顺" ,
        "即破发 丼","爱过几日 一体机","阿日贡 身体"]

for index,item in enumerate(team):
    if index%2 == 0:  #判断是否为偶数，为偶数时不换行
        print(item + "\t\t",end='')
    else:
        print(item + "\n")  #换行输出
