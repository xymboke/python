verse1 = ("一片冰心在玉壶",)
print('verse1的类型为',type(verse1))
verse2 = ("一片冰心在玉壶")
print('verse1的类型为',type(verse2))

print(tuple(range(10,20,2)))


print('==========================================')

coffeename = ('公平','供配电','狗蛋','配电柜','爱国','安静了')# 定义元组
print(coffeename)
print('==========================================')

untitle = ('python',28,'斯柯达','安静的','日光','爱福家','爱福家啊','爱神的箭')
print(untitle)
print(untitle[0])
print(untitle[:3])
print(untitle[3:])
print(untitle[1:3])
print(untitle[:])

print('===========================================')
verse = ('春眠不觉晓','阿拉斯加地方','就分手了','的房间里')
del verse
print(verse)
