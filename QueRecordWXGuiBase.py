# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class QueRecord 
###########################################################################

class QueRecord  ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"难题记忆", pos = wx.DefaultPosition, size = wx.Size( 637,536 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		QRBS = wx.BoxSizer( wx.VERTICAL )
		
		self.QRListBook = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.QSAdd = wx.Panel( self.QRListBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		addBS = wx.BoxSizer( wx.VERTICAL )
		
		self.addQueText = wx.TextCtrl( self.QSAdd, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,50 ), 0 )
		addBS.Add( self.addQueText, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.addConText = wx.TextCtrl( self.QSAdd, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,200 ), wx.TE_MULTILINE )
		addBS.Add( self.addConText, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.addUrlText = wx.TextCtrl( self.QSAdd, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		addBS.Add( self.addUrlText, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.addBt = wx.Button( self.QSAdd, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		addBS.Add( self.addBt, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		self.QSAdd.SetSizer( addBS )
		self.QSAdd.Layout()
		addBS.Fit( self.QSAdd )
		self.QRListBook.AddPage( self.QSAdd, u"添加", True )
		self.QRSearch = wx.Panel( self.QRListBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SBS = wx.BoxSizer( wx.VERTICAL )
		
		self.SkeywordsText = wx.TextCtrl( self.QRSearch, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		SBS.Add( self.SkeywordsText, 0, wx.ALL|wx.EXPAND, 5 )
		
		SLBChoices = []
		self.SLB = wx.ListBox( self.QRSearch, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,150 ), SLBChoices, wx.LB_ALWAYS_SB )
		SBS.Add( self.SLB, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.SConText = wx.TextCtrl( self.QRSearch, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		SBS.Add( self.SConText, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SUrl = wx.TextCtrl( self.QRSearch, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		SBS.Add( self.SUrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		SBSBtGS = wx.GridSizer( 0, 3, 0, 0 )
		
		self.SBtUpate = wx.Button( self.QRSearch, wx.ID_ANY, u"更新", wx.DefaultPosition, wx.DefaultSize, 0 )
		SBSBtGS.Add( self.SBtUpate, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.SBtDel = wx.Button( self.QRSearch, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		SBSBtGS.Add( self.SBtDel, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.SBtOpenUrl = wx.Button( self.QRSearch, wx.ID_ANY, u"打开链接", wx.DefaultPosition, wx.DefaultSize, 0 )
		SBSBtGS.Add( self.SBtOpenUrl, 0, wx.ALL, 5 )
		
		
		SBS.Add( SBSBtGS, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.QRSearch.SetSizer( SBS )
		self.QRSearch.Layout()
		SBS.Fit( self.QRSearch )
		self.QRListBook.AddPage( self.QRSearch, u"搜索", False )
		self.help = wx.Panel( self.QRListBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.helpText = wx.TextCtrl( self.help, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,300 ), wx.TE_MULTILINE )
		bSizer4.Add( self.helpText, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.savef = wx.StaticText( self.help, wx.ID_ANY, u"保存位置", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.savef.Wrap( -1 )
		bSizer4.Add( self.savef, 0, wx.ALL, 5 )
		
		self.DBfile = wx.TextCtrl( self.help, wx.ID_ANY, u"./styDB", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.DBfile, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.savefupdate = wx.Button( self.help, wx.ID_ANY, u"保存位置修改", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.savefupdate, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.authorsay = wx.StaticText( self.help, wx.ID_ANY, u"作者留言", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.authorsay.Wrap( -1 )
		bSizer4.Add( self.authorsay, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.help.SetSizer( bSizer4 )
		self.help.Layout()
		bSizer4.Fit( self.help )
		self.QRListBook.AddPage( self.help, u"帮助", False )
		
		QRBS.Add( self.QRListBook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( QRBS )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.addBt.Bind( wx.EVT_BUTTON, self.addBtOnButtonClick )
		self.SkeywordsText.Bind( wx.EVT_TEXT, self.SkeywordsTextOnText )
		self.SLB.Bind( wx.EVT_LISTBOX, self.SLBOnListBox )
		self.SBtUpate.Bind( wx.EVT_BUTTON, self.SBtUpateOnButtonClick )
		self.SBtDel.Bind( wx.EVT_BUTTON, self.SBtDelOnButtonClick )
		self.SBtOpenUrl.Bind( wx.EVT_BUTTON, self.SBtOpenUrlOnButtonClick )
		self.savefupdate.Bind( wx.EVT_BUTTON, self.savefupdateOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addBtOnButtonClick( self, event ):
		event.Skip()
	
	def SkeywordsTextOnText( self, event ):
		event.Skip()
	
	def SLBOnListBox( self, event ):
		event.Skip()
	
	def SBtUpateOnButtonClick( self, event ):
		event.Skip()
	
	def SBtDelOnButtonClick( self, event ):
		event.Skip()
	
	def SBtOpenUrlOnButtonClick( self, event ):
		event.Skip()
	
	def savefupdateOnButtonClick( self, event ):
		event.Skip()
	

