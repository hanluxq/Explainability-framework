import wx
import wx.xrc


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"上下文选择", pos=wx.DefaultPosition, size=wx.Size(756, 430),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"解释数据集", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        gbSizer2.Add(self.m_staticText1, wx.GBPosition(2, 4), wx.GBSpan(4, 10), wx.ALL, 5)

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1Yes = wx.Button(self.m_panel1, wx.ID_YES)
        m_sdbSizer1.AddButton(self.m_sdbSizer1Yes)
        self.m_sdbSizer1Help = wx.Button(self.m_panel1, wx.ID_HELP)
        m_sdbSizer1.AddButton(self.m_sdbSizer1Help)
        m_sdbSizer1.Realize()

        gbSizer2.Add(m_sdbSizer1, wx.GBPosition(2, 30), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.m_panel1.SetSizer(gbSizer2)
        self.m_panel1.Layout()
        gbSizer2.Fit(self.m_panel1)
        gbSizer1.Add(self.m_panel1, wx.GBPosition(1, 2), wx.GBSpan(8, 72), wx.EXPAND | wx.ALL, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText2 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"解释数据集", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        gbSizer3.Add(self.m_staticText2, wx.GBPosition(2, 4), wx.GBSpan(4, 10), wx.ALL, 5)

        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2Yes = wx.Button(self.m_panel2, wx.ID_YES)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Yes)
        self.m_sdbSizer2Help = wx.Button(self.m_panel2, wx.ID_HELP)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Help)
        m_sdbSizer2.Realize()

        gbSizer3.Add(m_sdbSizer2, wx.GBPosition(2, 30), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.m_panel2.SetSizer(gbSizer3)
        self.m_panel2.Layout()
        gbSizer3.Fit(self.m_panel2)
        gbSizer1.Add(self.m_panel2, wx.GBPosition(10, 2), wx.GBSpan(8, 72), wx.EXPAND | wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"上一页", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_button3, wx.GBPosition(19, 3), wx.GBSpan(4, 15), wx.ALL, 5)

        self.SetSizer(gbSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_sdbSizer1Help.Bind(wx.EVT_BUTTON, self.toDetail1)
        self.m_sdbSizer1Yes.Bind(wx.EVT_BUTTON, self.PageDown1)
        self.m_sdbSizer2Help.Bind(wx.EVT_BUTTON, self.toDetail2)
        self.m_sdbSizer2Yes.Bind(wx.EVT_BUTTON, self.PageDown2)
        self.m_button3.Bind(wx.EVT_BUTTON, self.PageUp)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def toDetail1(self, event):
        event.Skip()

    def PageDown1(self, event):
        event.Skip()

    def toDetail2(self, event):
        event.Skip()

    def PageDown2(self, event):
        event.Skip()

    def PageUp(self, event):
        event.Skip()
