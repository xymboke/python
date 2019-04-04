'''
问题：图形化界面，设计3个按钮，对应功能分别为(1)计算1+2+...+n;(2)在文本框中输入
一些数，求最大值;(3)在文本框中输入一些数，排序
作者：xymoke
地点：D215
时间：
'''
import wx
class Frame3(wx.Frame):
    def __init__(self,superion):
        wx.Frame.__init__(self,parent=superion,title=u"通过文本框输入和输出",size=(800,500))
        panel=wx.Panel(self)
        #在panel上放置静态文框
        wx.StaticText(parent=panel,label=u"输入n:",pos=(10,10))
        #在panel上放置文本框，用于接收用户给变量n输入的值
        self.inputN=wx.TextCtrl(parent=panel,pos=(150,10))
        #在panel上放置静态文本框
        wx.StaticText(parent=panel,label=u"1累加到n的结果为：",pos=(10,50))
        wx.StaticText(parent=panel,label=u"最大值为：",pos=(10,100))
        wx.StaticText(parent=panel,label=u"排序为：",pos=(10,150))
        #在panel上放置文本框，用于输出计算结果
        self.outSum=wx.TextCtrl(parent=panel,pos=(150,50),size=(450,30))
        self.outmax=wx.TextCtrl(parent=panel,pos=(150,100),size=(450,30))
        self.outsort=wx.TextCtrl(parent=panel,pos=(150,150),size=(450,30))
        #在panel上放置命令按钮，用于生产单击事件
        self.btnSum=wx.Button(parent=panel,label=u"计算",pos=(350,300),size=(50,30))
        self.btnmax=wx.Button(parent=panel,label=u"最大值",pos=(400,300),size=(100,30))
        self.btnsort=wx.Button(parent=panel,label=u"排序",pos=(450,300),size=(150,30))
        #将命令按钮的单击事件与f函数绑定。这样，单击按钮时就会调用该函数
        self.Bind(wx.EVT_BUTTON,self.f,self.btnSum)
        self.Bind(wx.EVT_BUTTON,self.g,self.btnmax)
        self.Bind(wx.EVT_BUTTON,self.h,self.btnsort)
    #定义成员函数f，计算从1累加到n的结果
    def f(self,event):
        n=self.inputN.GetValue() #获得文本框inputN中的输入内容，是一个串
        n=int(n)
        i=1
        s=0
        while i<=n:
            s=s+i
            i +=1
        self.outSum.SetValue(str(s))  #向文本框outsum输出一个串
    def g(self,event):
        n=self.inputN.GetValue()
        b = list(eval(n))
        c = max(b)
        self.outmax.SetValue(str(c))
    def h(self,event):
        n= eval(self.inputN.GetValue())
        n = list(n)
        n.sort()
        self.outsort.SetValue(str(n))
          
     
#主程序
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=Frame3(None)
    frame.Show(True)
    app.MainLoop()
