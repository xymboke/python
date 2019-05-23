coffeename = ('拉克丝的','阿莎','昂','拉上来','案件是否','打发时间','卡视角','卡机是')
print("您好，欢迎光临-拉丝看得见-\n\n我店有：\n")
for name in coffeename:  #遍历元组
    print(name + "咖啡" ,end= " ")



print("2017至2018赛季NBA西部联盟前八名\n")
team = ("火箭","勇士","开拓者","雷霆","爵士","鹈鹕","马刺","森林狼")
for index,item in enumerate(team):
    if index%2 == 0:     #判断是否为偶数，为偶数时不换行
        print(item + "\t\t",end='')
    else:
        print(item + "\n") #换行输出
