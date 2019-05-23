import os
path="H:\\资料总整理\\python\\10基础\\10 文件及目录操作\\目录操作\\e"  #指定要创建的目录
if os.path.exists(path):          #判断目录是否存在
    os.rmdir("H:\\资料总整理\\python\\10基础\\10 文件及目录操作\\目录操作\\e") #删除目录
    print("目录删除成功！")
else:
    print("该目录不存在")
