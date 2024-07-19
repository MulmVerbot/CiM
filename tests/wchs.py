import wx

class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget

    def OnDropFiles(self, x, y, filenames):
        self.widget.SetLabel(filenames[0])

class MyFrame(wx.Frame):
    def __init__(self):
        frame = MyFrame()
        frame.Show()
        super().__init__(None, title="wxPython Drag and Drop")
        panel = wx.Panel(self)
        self.label = wx.StaticText(panel, label="Drag a file here", pos=(10,10))
        drop_target = MyFileDropTarget(frame)
        self.label.SetDropTarget(drop_target)

app = wx.App(False)

app.MainLoop()
