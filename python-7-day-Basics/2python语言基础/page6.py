print("\n手机店正在打折，活动进行中……")
strWeek=input("请输入中文星期（如星期一）：")
intTime=int(input("请输入时间中的小时（范围：0到23）"))

if (strWeek == "星期二" and (intTime >= 10 and intTime <= 11)) or (strWeek == "星期五"
    and (intTime >= 14 and intTime <= 15)):
    print("恭喜")
else:
    print("对不起")
