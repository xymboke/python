import os

src="demo"   #重命名的当前目录下的demo

dst="test"   #重命名为test

if os.path.exists(src):    #判断目录是否存在
    os.rename(src,dst)     #重命名目录
    print("目录重命名完毕！")
else:
    print("目录不存在！")
