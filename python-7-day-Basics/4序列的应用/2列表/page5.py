phone = ["喀斯柯达","大胜靠德","符号开始","圣诞节"]
print(len(phone))  #获取列表长度
phone.append("iphone")
print(len(phone)) #获取列表长度
print(phone)
print("="*40)
phone2 = ["喀斯柯达","大胜靠德","符号开始","圣诞节"]
phone1=["豆腐皮","底盘的","阿莎看","爱干净","爱神的箭"] #新增人员列表
phone2.extend(phone1)  #追加新
print(phone2)
