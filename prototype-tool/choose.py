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
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"文件选择", pos=wx.DefaultPosition, size=wx.Size(756, 430),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer4 = wx.GridBagSizer(0, 0)
        gbSizer4.SetFlexibleDirection(wx.BOTH)
        gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel7.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        gbSizer5 = wx.GridBagSizer(0, 0)
        gbSizer5.SetFlexibleDirection(wx.BOTH)
        gbSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText3 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"选择文件", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        gbSizer5.Add(self.m_staticText3, wx.GBPosition(2, 12), wx.GBSpan(4, 10), wx.ALL, 5)

        self.m_button2 = wx.Button(self.m_panel7, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer5.Add(self.m_button2, wx.GBPosition(2, 38), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_panel7.SetSizer(gbSizer5)
        self.m_panel7.Layout()
        gbSizer5.Fit(self.m_panel7)
        gbSizer4.Add(self.m_panel7, wx.GBPosition(5, 2), wx.GBSpan(8, 72), wx.EXPAND | wx.ALL, 5)

        self.SetSizer(gbSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


