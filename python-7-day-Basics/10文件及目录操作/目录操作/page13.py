import os

path = "H:\\资料总整理\\python\\10基础\\10 文件及目录操作\\目录操作" #指定要遍历的根目录

print("【",path,"】 目录下包括的文件和目录: ")

for root, dirs, files in os.walk(path, topdown=True):  #遍历指定目录
    for name in dirs:    #循环输出遍历到子目录
        print("@",os.path.join(root,name))
    for name in files:   #循环输出遍历到文件
        print("$",os.path.join(root,name))
