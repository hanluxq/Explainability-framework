import xmindparser
import wx
import wx.xrc
# import result
import os
# import sklearn
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# import numpy as np
# import shap

def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


# 得到根节点
def getRootVal(root):
    return root[0]


# 设立根节点
def setRootVal(root, newVal):
    root[0] = newVal


# 得到左子树
def getLeftChild(root):
    return root[1]


# 得到右子树
def getRightChild(root):
    return root[2]


# 根据字典创建二叉树
def createBiTree(tempdict, temproot):
    setRootVal(temproot, tempdict['title'])
    if 'topics' in tempdict:
        insertLeft(temproot, "")
        createBiTree(tempdict['topics'][0], getLeftChild(temproot))
        if len(tempdict['topics']) == 2:
            insertRight(temproot, "")
            createBiTree(tempdict['topics'][1], getRightChild(temproot))


# 根据二叉树创建树形列表
def createTree(filePath):
    content = xmindparser.xmind_to_dict(filePath)
    dictTree = content[0]['topic']
    tree = BinaryTree("")
    createBiTree(dictTree, tree)
    print(tree)
    return tree


class Choose(wx.Frame):
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

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.FileChoose)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def FileChoose(self, event):
        wildcard = 'All files(*.*)|*.*'
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard, wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            filePath = dialog.GetPath()
            print(filePath)
            tree = createTree(filePath)
            dialog.Destroy
            app = wx.App(False)
            frame = Selection(None, tree)
            Selection.Textupdate(frame, getRootVal(getLeftChild(tree)), getRootVal(getRightChild(tree)))
            frame.Show(True)
            app.MainLoop()


class Selection(wx.Frame):
    def __init__(self, parent, tree):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"上下文选择", pos=wx.DefaultPosition, size=wx.Size(756, 430),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.treenode = tree
        self.initTree = tree
        self.ch = ''
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

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
        wildcard = 'All files(*.*)|*.*'
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard, wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            filePath = dialog.GetPath()
            print(filePath)
            DetailTree = createTree(filePath)
            dialog.Destroy
            app = wx.App(False)
            frame = DetailChoose(None, DetailTree)
            DetailChoose.Textupdate(frame, getRootVal(getLeftChild(DetailTree)), getRootVal(getRightChild(DetailTree)))
            frame.Show(True)
            app.MainLoop()
        # event.Skip()

    def PageDown1(self, event):
        if getLeftChild(self.treenode) is not None and getRightChild(self.treenode) is not None:
            self.treenode = getLeftChild(self.treenode)
            self.ch += 'l'
            self.Textupdate(getRootVal(getLeftChild(self.treenode)), getRootVal(getRightChild(self.treenode)))
        # elif getRightChild(self.treenode) is None:
        #     # turn to result
        # event.Skip()

    def toDetail2(self, event):
        wildcard = 'All files(*.*)|*.*'
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard, wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            filePath = dialog.GetPath()
            print(filePath)
            DetailTree = createTree(filePath)
            dialog.Destroy
            app = wx.App(False)
            frame = DetailChoose(None, DetailTree)
            Selection.Textupdate(frame, getRootVal(getLeftChild(DetailTree)), getRootVal(getRightChild(DetailTree)))
            frame.Show(True)
            app.MainLoop()
        # event.Skip()

    def PageDown2(self, event):
        if getLeftChild(self.treenode) is not None and getRightChild(self.treenode) is not None:
            self.treenode = getRightChild(self.treenode)
            self.ch += 'r'
            self.Textupdate(getRootVal(getLeftChild(self.treenode)), getRootVal(getRightChild(self.treenode)))
        # elif getRightChild(self.treenode) is None:
        #     # turn to result
        # event.Skip()

    def PageUp(self, event):
        event.Skip()
        # self.treenode = self.initTree
        # for i in range(len(self.ch) - 1):
        #     if self.ch[i] == 'l':
        #         self.treenode = getLeftChild(self.treenode)
        #     else:
        #         self.treenode = getRightChild(self.treenode)
        # self.ch = self.ch[:-1]
        # self.Textupdate(getRootVal(getLeftChild(self.treenode)), getRootVal(getRightChild(self.treenode)))


    def Textupdate(self, text1, text2):
        self.m_staticText1.Label = text1
        self.m_staticText2.Label = text2


class DetailChoose(wx.Frame):

    def __init__(self, parent, tree):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"分解选择", pos=wx.DefaultPosition, size=wx.Size(756, 430),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.treenode = tree
        self.initTree = tree
        self.ch = ''
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
        if getLeftChild(self.treenode) is not None and getRightChild(self.treenode) is not None:
            self.treenode = getLeftChild(self.treenode)
            self.Textupdate(getRootVal(getLeftChild(self.treenode)), getRootVal(getRightChild(self.treenode)))
        # elif getRightChild(self.treenode) is None:
        #     # turn to result
        # event.Skip()

    def PageDown2(self, event):
        if getLeftChild(self.treenode) is not None and getRightChild(self.treenode) is not None:
            self.treenode = getRightChild(self.treenode)
            self.Textupdate(getRootVal(getLeftChild(self.treenode)), getRootVal(getRightChild(self.treenode)))
        # elif getRightChild(self.treenode) is None:
        #     # turn to result
        # event.Skip()

    def PageUp(self, event):
        event.Skip()
        # self.treenode = self.initTree
        # for i in range(len(self.ch) - 1):
        #     if self.ch[i] == 'l':
        #         self.treenode = getLeftChild(self.treenode)
        #     else:
        #         self.treenode = getRightChild(self.treenode)
        # self.ch = self.ch[:-1]
        # self.Textupdate(getRootVal(getLeftChild(self.treenode)), getRootVal(getRightChild(self.treenode)))

    def Textupdate(self, text1, text2):
        self.m_staticText4.Label = text1
        self.m_staticText5.Label = text2


class Result(wx.Frame):
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

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"上一页", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.m_button3, wx.GBPosition(17, 3), wx.GBSpan(4, 15), wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"返回首页", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.m_button4, wx.GBPosition(17, 55), wx.GBSpan(4, 15), wx.ALL, 5)

        self.SetSizer(gbSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button3.Bind(wx.EVT_BUTTON, self.PageUp)
        self.m_button4.Bind(wx.EVT_BUTTON, self.firstPage)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def PageUp(self, event):
        event.Skip()

    def firstPage(self, event):
        event.Skip()


class MyApp(wx.App):
    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        super().__init__(redirect, filename, useBestVisual, clearSigInt)
        self.myframe2 = None
        self.myframe = None

    def OnInit(self):
        self.myframe = Selection(None)
        self.myframe2 = Result(None)
        self.SetTopWindow(self.myframe)
        self.myframe.Show(True)
        self.myframe2.Show(True)
        return True


def main():
    # xmindparser配置
    xmindparser.config = {
        'showTopicId': True,  # 是否展示主题ID
        'hideEmptyValue': True  # 是否隐藏空值
    }

    # filePath = '../xmind/test1.xmind'
    # filePath = 'D:\\capstone\\程序\\xmind\\test1.xmind'
    # content = xmindparser.xmind_to_dict(filePath)
    # dictTree = content[0]['topic']
    # tree = BinaryTree("")
    # createBiTree(dictTree, tree)
    # print(tree)
    app = wx.App(False)
    frame = Choose(None)
    # frame = Selection(None, tree)
    # Selection.Textupdate(frame, getRootVal(getLeftChild(tree)), getRootVal(getRightChild(tree)))
    frame.Show(True)
    # start the applications
    app.MainLoop()


if __name__ == '__main__':
    main()


# corpus,y = shap.datasets.imdb()
# corpus_train, corpus_test, y_train, y_test = train_test_split(corpus, y, test_size=0.2, random_state=7)
#
# vectorizer = TfidfVectorizer(min_df=10)
# X_train = vectorizer.fit_transform(corpus_train).toarray() # sparse also works but Explanation slicing is not yet supported
# X_test = vectorizer.transform(corpus_test).toarray()
#
# model = sklearn.linear_model.LogisticRegression(penalty="l2", C=0.1)
# model.fit(X_train, y_train)
#
# explainer = shap.Explainer(model, X_train, feature_names=vectorizer.get_feature_names())
# shap_values = explainer(X_test)
#
# shap.plots.beeswarm(shap_values)#, X_test_array, feature_names=vectorizer.get_feature_names())
#
# ind = 0
# shap.plots.force(shap_values[ind])
#
# print("Positive" if y_test[ind] else "Negative", "Review:")
# print(corpus_test[ind])
#
# ind = 1
# shap.plots.force(shap_values[ind])
#
# print("Positive" if y_test[ind] else "Negative", "Review:")
# print(corpus_test[ind])
#
# ind = 2
# shap.plots.force(shap_values[ind])
#
# print("Positive" if y_test[ind] else "Negative", "Review:")
# print(corpus_test[ind])