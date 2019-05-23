phone = ["喀斯柯达","大胜靠德","符号开始","圣诞节"]
print(phone)
phone[2]="一行白鹭上青天"
print(phone)

print("::"*30)
del phone[-1]
print(phone)

print("::"*30)
value="一行白鹭上青天" #指定要移动的元素
if phone.count(value)>0:  #判断要删除的元素是否存在
    phone.remove(value) #移除指定的元素
print(phone)


print("::"*30)
phone.remove("大胜靠得")
print(phone)
