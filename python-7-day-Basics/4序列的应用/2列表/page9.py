'''
verse = [['千','山','鸟','飞','绝'],['万','径','人','踪','灭'],
         ['孤','舟','蓑','笠','翁'],['独','钓','寒','江','雪']]
'''

arr = []  #创建一个空列表
for i in range(4):
    arr.append([])  #在空列表中再添加一个空列表
    for j in range(5):
        arr[i].append(j) #为内层列表添加元素
print(arr)


arr = [[j for j in range(5)] for i in range(4)]
print(arr)
