

# Qt libraries
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

qtcreator_file  = "sherlockGUI.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


##
# @brief    Audmerge Class
# @details  TODO
#
# @param    QtWidgets.QMainWindow       TODO
# @param    Ui_MainWindow               TODO
class AudmergeWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    # Variables

    ##
    # @brief    Name of the splitted output files
    # @details  The single files will be appended by _#
    split_outputNameString = ""

    ##
    # @brief    Init
    # @details  TODO
    #
    # @param    self    Object itself
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)



        # Setup #


        # Connections #





##
# @brief    Main Call
# @details  TODO
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AudmergeWindow()
    window.setWindowIcon( QtGui.QIcon('icons/favicon.ico') )
    window.show()
    sys.exit(app.exec_())
