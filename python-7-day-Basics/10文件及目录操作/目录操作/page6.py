import os
path = "H:\\资料总整理\\python\\10基础\\10 文件及目录操作\\目录操作\\exe" #指定要创建的目录
if not os.path.exists(path): #判断目录是否存在
    os.mkdir(path) #创建exe新目录
    print("目录创建成功")
else:
    print("该目录已经存在！")
