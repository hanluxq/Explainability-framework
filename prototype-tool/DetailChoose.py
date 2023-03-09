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
## Class DetailChoose
###########################################################################

class DetailChoose(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"分解选择", pos=wx.DefaultPosition, size=wx.Size(756, 430),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer6 = wx.GridBagSizer(0, 0)
        gbSizer6.SetFlexibleDirection(wx.BOTH)
        gbSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panel8 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel8.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        gbSizer7 = wx.GridBagSizer(0, 0)
        gbSizer7.SetFlexibleDirection(wx.BOTH)
        gbSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText4 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"解释数据集", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        gbSizer7.Add(self.m_staticText4, wx.GBPosition(2, 4), wx.GBSpan(4, 10), wx.ALL, 5)

        self.m_button4 = wx.Button(self.m_panel8, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.m_button4, wx.GBPosition(2, 30), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_panel8.SetSizer(gbSizer7)
        self.m_panel8.Layout()
        gbSizer7.Fit(self.m_panel8)
        gbSizer6.Add(self.m_panel8, wx.GBPosition(1, 2), wx.GBSpan(8, 72), wx.EXPAND | wx.ALL, 5)

        self.m_panel10 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel10.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        gbSizer8 = wx.GridBagSizer(0, 0)
        gbSizer8.SetFlexibleDirection(wx.BOTH)
        gbSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"解释数据集", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        gbSizer8.Add(self.m_staticText5, wx.GBPosition(2, 4), wx.GBSpan(4, 10), wx.ALL, 5)

        self.m_button5 = wx.Button(self.m_panel10, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_button5, wx.GBPosition(2, 30), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_panel10.SetSizer(gbSizer8)
        self.m_panel10.Layout()
        gbSizer8.Fit(self.m_panel10)
        gbSizer6.Add(self.m_panel10, wx.GBPosition(10, 2), wx.GBSpan(8, 72), wx.EXPAND | wx.ALL, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"上一页", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer6.Add(self.m_button6, wx.GBPosition(19, 3), wx.GBSpan(4, 15), wx.ALL, 5)

        self.SetSizer(gbSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button4.Bind(wx.EVT_BUTTON, self.PageDown1)
        self.m_button5.Bind(wx.EVT_BUTTON, self.PageDown2)
        self.m_button6.Bind(wx.EVT_BUTTON, self.PageUp)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def PageDown1(self, event):
        event.Skip()

    def PageDown2(self, event):
        event.Skip()

    def PageUp(self, event):
        event.Skip()


