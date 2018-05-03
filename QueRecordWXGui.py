import QueRecordWXGuiBase as qr
import sdydata as sd
import wx  
import wx.xrc 
import webbrowser
import warnings
warnings.filterwarnings("ignore")



class QRWG(qr.QueRecord):
	def __init__(self,parent):
		qr.QueRecord.__init__(self,parent)
		self.url = self.DBfile.GetValue()
		self.DB = sd.SdyDB(self.url)
		self.ontherInit()
	def __del__(self):
		pass
	def addBtOnButtonClick( self, event ):
		quetion = self.addQueText.GetValue()
		if quetion == "":
			wx.MessageBox("问题不能为空啊HuaQ", caption="add", style=wx.OK)
		content = self.addConText.GetValue()
		URL = self.addUrlText.GetValue()
		tempdata = sd.sdydata(content,URL)
		try:
			self.DB.addQC(quetion,tempdata)		
		except sd.QueRepeError as se:
			wx.MessageBox("重复了!,自动修改问题", caption="add", style=wx.OK)
			self.addQueText.SetValue(self.addQueText.GetValue() +"-"+  str(self.DB.getSum()))
		except Exception as e:
			wx.MessageBox(str(e), caption="add", style=wx.OK)
		else:
			wx.MessageBox("添加成功", caption="add", style=wx.OK)
			self.addQueText.SetValue("")
			self.addConText.SetValue("")
			self.addUrlText.SetValue("")
			self.SkeywordsText.SetValue(self.SkeywordsText.GetValue() + "")
		event.Skip()
	
	def SkeywordsTextOnText( self, event ):
		kws = self.SkeywordsText.GetValue()
		kwlist = kws.split(';')
		ques = self.DB.searchQC(kwlist)
		self.SLB.Set(ques) 
		event.Skip()
	
	def SLBOnListBox( self, event ):
		queTemp = self.SLB.GetStringSelection()
		data = self.DB.getContent(queTemp)
		self.SConText.SetValue(data.content)
		self.SUrl.SetValue(data.url)
		event.Skip()
	def SBtUpateOnButtonClick( self, event ):
		queTemp = self.SLB.GetStringSelection()
		if queTemp == "":
			return
		content = self.SConText.GetValue()
		url = self.SUrl.GetValue()
		tempdata = sd.sdydata(content,url)
		try:
			self.DB.updateQC(queTemp,tempdata)
		except Exception as e:
			wx.MessageBox(str(e), caption="update", style=wx.OK)
		else:
			wx.MessageBox("更新成功", caption="update", style=wx.OK)
		event.Skip()
	
	def SBtDelOnButtonClick( self, event ):
		queTemp = self.SLB.GetStringSelection()
		if queTemp == "":
			return
		try:
			self.DB.delQC(queTemp)
		except Exception as e:
			wx.MessageBox(str(e), caption="del", style=wx.OK)
		else:
			#wx.MessageBox("删除成功", caption="update", style=wx.OK)
			self.SkeywordsText.SetValue(self.SkeywordsText.GetValue() + "")
			self.SConText.SetValue("")
			self.SUrl.SetValue("")
		event.Skip()
	
	def SBtOpenUrlOnButtonClick( self, event ):
		url = self.SUrl.GetValue()
		if not url == "":
			webbrowser.open(url)
		event.Skip()
	
	def savefupdateOnButtonClick( self, event ):
		if self.DBfile.GetValue() == "":
			self.DBfile.SetValue("./styDB")
			self.url = "./styDB"
		else:
			self.url = self.DBfile.GetValue()
			self.DB = sd.SdyDB(self.url)		
		self.SkeywordsText.SetValue("")
		self.SLB.Set([""])
		self.SConText.SetValue("")
		self.SUrl.SetValue("")
		event.Skip()
	def ontherInit(self):
		helptxt = "懒得写了"
		self.helpText.SetValue(helptxt)
		authorSay = "huaQ"
		self.authorsay.SetLabel("作者的话:\r\n"+authorSay)




if __name__ == "__main__":
	try:
		app = wx.App()  	    
		main_win = QRWG(None)  
		main_win.Show(True)  
		app.MainLoop()  
	except BaseException as e:
		pass
	finally:
		del app

