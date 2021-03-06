# coding=utf-8
# foreign
from qtpy import QtGui, QtPrintSupport, QtWidgets, QtCore
# this pkg
from ._textEditorUtils import ToolBarFormat, ToolBarFont, ToolBarInsert, MainWindow


class FwMinimalTextEditor(MainWindow):

    def __init__(self, parent=None):
        MainWindow.__init__(self, parent)

        self.text.setTabStopWidth(12)
        self.setCentralWidget(self.text)
        self.addToolBar(ToolBarFont(self.text))
        toolBarInsert = ToolBarInsert(self.text)
        self.addToolBar(toolBarInsert)
        self.addToolBarBreak()
        toolBar = ToolBarFormat(self.text)
        self.addToolBar(toolBar)

        toolBarInsert.setIconSize(QtCore.QSize(16, 16))
        toolBar.setIconSize(QtCore.QSize(16, 16))
        # self.setGeometry(100,100,700,700)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = FwMinimalTextEditor()
    w.setWindowTitle(w.__class__.__name__)

    w.show()
    app.exec_()
