import os

src="H:\\资料总整理\\python\\10基础\\10 文件及目录操作\\目录操作\\e.txt" #要重要命名的文件

dst="H:\\资料总整理\\python\\10基础\\10 文件及目录操作\\目录操作\\mr.txt" #重命名后的文件

os.rename(src,dst)            #重命名文件
if os.path.exists(src):   #判断文件是否存在
    os.rename(src,dst) #重命名文件
    print("文件重命名完毕！")
else:
    print("文件不存在！")
    
