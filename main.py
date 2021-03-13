

# Qt libraries
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import webbrowser

from socialMediaProfile import socialMediaProfile

qtcreator_file  = "sherlockGUI.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


##
# @brief    SherlockGUI Class
# @details  TODO
#
# @param    QtWidgets.QMainWindow       TODO
# @param    Ui_MainWindow               TODO
class SherlockGUIWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    # Variables
    webpages = {
        "facebook" : "https://www.facebook.com"
    }

    class socials:
        facebook = socialMediaProfile("https://www.facebook.com/")
        instagram = socialMediaProfile("https://www.instagram.com/")

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

        self.deactivateAllSocialBtns()



        # Setup #


        # Connections #
        self.btn_facebook.clicked.connect(self.openFacebook)
        self.btn_investigate.clicked.connect(self.investigate)


    def deactivateAllSocialBtns(self):
        self.btn_facebook.setEnabled(False)
        self.btn_instagram.setEnabled(False)

    def opensite(self, string):
        webbrowser.open(string)

    def openFacebook(self):
        self.opensite(self.socials.facebook.getlink2Profile())

    def investigate(self):
        print("Investigation started")

        # deactivate button until investigation finished
        self.btn_investigate.setEnabled(False)

        print("Investigation finished")
        self.btn_investigate.setEnabled(True)



    ##
# @brief    Main Call
# @details  TODO
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SherlockGUIWindow()
    window.show()
    sys.exit(app.exec_())
