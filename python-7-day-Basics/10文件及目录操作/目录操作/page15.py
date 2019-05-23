import os

path = "er.txt"    #要删除的文件

if os.path.exists(path):   #判断文件是否存在
    os.remove(path)        #删除文件
    print("文件删除完毕！")
else:
    print("文件不存在！")
