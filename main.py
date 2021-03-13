

# Qt libraries
import os
import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import webbrowser

from socialMediaProfile import socialMediaProfile
from sherlockAdapter import sherlockAdapter


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

    sherlock = sherlockAdapter()

    class socials:
        facebook = socialMediaProfile("https://www.facebook.com/", "facebook")
        instagram = socialMediaProfile("https://www.instagram.com/", "instagram")

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

        self.btn_openResults.clicked.connect(self.openResultFile)


    def deactivateAllSocialBtns(self):
        self.btn_facebook.setEnabled(False)
        self.btn_instagram.setEnabled(False)

    def opensite(self, string):
        webbrowser.open(string)

    def openFacebook(self):
        self.opensite(self.socials.facebook.getlink2Profile())

    def checkWantedProfiles(self):
        if self.check_facebook.isChecked() :
            sherlockAdapter.addSearchProfile("facebook")
        if self.check_instagram.isChecked():
            sherlockAdapter.addSearchProfile("instagram")

    def checkUsername(self):
        self.sherlock.addUsername(self.input_name.text())

    def investigate(self):
        print("Investigation started")

        # deactivate button until investigation finished
        self.btn_investigate.setEnabled(False)

        self.checkUsername()

        self.checkWantedProfiles()

        self.sherlock.setTimeout(self.input_timeout.value())

        self.sherlock.investigate()

        print("Investigation finished")
        self.btn_investigate.setEnabled(True)

    def openResultFile(self):
        filename = "discoveries.txt"
        webbrowser.open(filename)




    ##
# @brief    Main Call
# @details  TODO
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SherlockGUIWindow()
    window.show()
    sys.exit(app.exec_())
