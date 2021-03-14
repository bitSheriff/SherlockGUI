

# Qt libraries
import os
import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import webbrowser
import csv
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


    socials = {
        "facebook" : socialMediaProfile("https://www.facebook.com/", "facebook"),
        "instagram" : socialMediaProfile("https://www.instagram.com/", "instagram")
    }

    ##
    # @brief    Init
    # @details  TODO
    #
    # @param    self    Object itself
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.deactivateBrokenSocials()
        self.deactivateAllSocialBtns()



        # Setup #


        # Connections #
        self.btn_facebook.clicked.connect(self.openFacebook)
        self.btn_investigate.clicked.connect(self.investigate)

        self.btn_openResults.clicked.connect(self.openResultFile)

    def deactivateBrokenSocials(self):
        self.btn_instagram.setEnabled(False)
        self.check_instagram.enable = False

    def deactivateAllSocialBtns(self):
        self.btn_facebook.setEnabled(False)
        self.btn_instagram.setEnabled(False)

    def opensite(self, string):
        webbrowser.open(string)

    def openFacebook(self):
        self.opensite(self.socials["facebook"].getlink2Profile())

    def checkWantedProfiles(self):
        if self.check_facebook.isChecked() :
            self.sherlock.addSearchProfile("facebook")
        if self.check_instagram.isChecked():
            self.sherlock.addSearchProfile("instagram")

    def setFoundProfileBtns(self):
        if self.socials["facebook"].link2Profile != "":
            self.btn_facebook.setEnabled(True)

    def checkUsername(self):
        self.sherlock.addUsername(self.input_name.text())

    def investigate(self):
        print("Investigation started")

        # deactivate button until investigation finished
        self.btn_investigate.setEnabled(False)

        # deactivate all social buttons for new search
        self.deactivateBrokenSocials()

        # send the username to the sherlock adapter
        self.checkUsername()

        # send the wanted social media profiles to sherlock adapter
        self.checkWantedProfiles()

        # configure the timeout
        self.sherlock.setTimeout(self.input_timeout.value())

        # start sherlock
        self.sherlock.investigate()

        # read the csv of the searched social media profiles
        self.readCSV()

        # activate the buttons of the found profiles
        self.setFoundProfileBtns()

        print("Investigation finished")
        self.btn_investigate.setEnabled(True)

    def openResultFile(self):
        filename = "discoveries.txt"
        webbrowser.open(filename)

    def readCSV(self):
        with open("Benjamin.Mandl.csv") as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                if row[6] == "response_time_s":
                    continue
                try:
                    self.socials[str(row[1]).lower()].status = str(row[5])
                    self.socials[str(row[1]).lower()].link2Profile = str(row[3])
                except KeyError:
                    print("Entry not found")



                ##
# @brief    Main Call
# @details  TODO
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SherlockGUIWindow()
    window.show()
    sys.exit(app.exec_())
