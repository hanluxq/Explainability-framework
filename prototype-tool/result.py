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
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"结果显示", pos=wx.DefaultPosition, size=wx.Size(756, 430),
						  style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

		gbSizer4 = wx.GridBagSizer(0, 0)
		gbSizer4.SetFlexibleDirection(wx.BOTH)
		gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

		gbSizer6 = wx.GridBagSizer(0, 0)
		gbSizer6.SetFlexibleDirection(wx.BOTH)
		gbSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText1 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"推荐结果：", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText1.Wrap(-1)
		self.m_staticText1.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

		gbSizer6.Add(self.m_staticText1, wx.GBPosition(1, 3), wx.GBSpan(4, 10), wx.ALL, 5)

		self.m_staticText8 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"TBD", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText8.Wrap(-1)
		self.m_staticText8.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))

		gbSizer6.Add(self.m_staticText8, wx.GBPosition(5, 5), wx.GBSpan(4, 10), wx.ALL, 5)

		self.m_panel5.SetSizer(gbSizer6)
		self.m_panel5.Layout()
		gbSizer6.Fit(self.m_panel5)
		gbSizer4.Add(self.m_panel5, wx.GBPosition(1, 2), wx.GBSpan(15, 72), wx.EXPAND | wx.ALL, 5)

		self.m_button4 = wx.Button(self, wx.ID_ANY, u"返回首页", wx.DefaultPosition, wx.DefaultSize, 0)
		gbSizer4.Add(self.m_button4, wx.GBPosition(17, 55), wx.GBSpan(4, 15), wx.ALL, 5)

		self.SetSizer(gbSizer4)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_button4.Bind(wx.EVT_BUTTON, self.firstPage)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def firstPage(self, event):
		event.Skip()
	

