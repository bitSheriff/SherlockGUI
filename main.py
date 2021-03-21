

# Qt libraries
import os
import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QRegExpValidator
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
        "facebook":     socialMediaProfile("facebook"),
        "reddit":       socialMediaProfile("reddit"),
        "twitch":       socialMediaProfile("twitch"),
        "twitter":      socialMediaProfile("twitter"),
        "google":       socialMediaProfile("google"),
        "skype":        socialMediaProfile("skype"),
        "spotify":      socialMediaProfile("spotify"),
        "telegram":     socialMediaProfile("telegram"),
        "tiktok":       socialMediaProfile("tiktok"),
        "tinder":       socialMediaProfile("tinder"),
        "strava":       socialMediaProfile("strava"),
        "instagram":    socialMediaProfile("instagram")
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
        rx = QRegExp("[a-zA-Z]*[0-9]*\_*\-*")
        self.input_name.setValidator(QRegExpValidator(rx))

        # Connections #
        self.btn_facebook.clicked.connect(self.openFacebook)
        self.btn_reddit.clicked.connect(self.openReddit)
        self.btn_twitch.clicked.connect(self.openTwitch)
        self.btn_twitter.clicked.connect(self.openTwitter)
        self.btn_google.clicked.connect(self.openGoogle)
        self.btn_skype.clicked.connect(self.openSkype)
        self.btn_spotify.clicked.connect(self.openSpotify)
        self.btn_telegram.clicked.connect(self.openTelegram)
        self.btn_tiktok.clicked.connect(self.openTiktok)
        self.btn_tinder.clicked.connect(self.openTinder)
        self.btn_strava.clicked.connect(self.openStrava)

        self.btn_investigate.clicked.connect(self.investigate)
        self.btn_trashbin.clicked.connect(self.trashBinClear)
        self.btn_openResults.clicked.connect(self.openResultFile)

        self.webView.load("ww.google.at")

    def deactivateBrokenSocials(self):
        self.btn_instagram.setEnabled(False)
        self.check_instagram.enable = False

    def deactivateAllSocialBtns(self):
        self.btn_facebook.setEnabled(False)
        self.btn_instagram.setEnabled(False)
        self.btn_reddit.setEnabled(False)
        self.btn_twitch.setEnabled(False)
        self.btn_twitter.setEnabled(False)
        self.btn_google.setEnabled(False)
        self.btn_skype.setEnabled(False)
        self.btn_spotify.setEnabled(False)
        self.btn_telegram.setEnabled(False)
        self.btn_tiktok.setEnabled(False)
        self.btn_tinder.setEnabled(False)
        self.btn_strava.setEnabled(False)

    def deactivateAllInputFields(self):
        self.input_name.setText("")
        self.check_facebook.setChecked(False)
        self.check_instagram.setChecked(False)
        self.check_reddit.setChecked(False)
        self.check_twitch.setChecked(False)
        self.check_twitter.setChecked(False)
        self.check_google.setChecked(False)
        self.check_skype.setChecked(False)
        self.check_spotify.setChecked(False)
        self.check_telegram.setChecked(False)
        self.check_tiktok.setChecked(False)
        self.check_tinder.setChecked(False)
        self.check_strava.setChecked(False)

    def opensite(self, string):
        webbrowser.open(string)

    def openFacebook(self):
        self.opensite(self.socials["facebook"].getlink2Profile())

    def openReddit(self):
        self.opensite(self.socials["reddit"].getlink2Profile())

    def openTwitch(self):
        self.opensite(self.socials["twitch"].getlink2Profile())

    def openTwitter(self):
        self.opensite(self.socials["twitter"].getlink2Profile())

    def openGoogle(self):
        self.opensite(self.socials["google"].getlink2Profile())

    def openSkype(self):
        self.opensite(self.socials["skype"].getlink2Profile())

    def openSpotify(self):
        self.opensite(self.socials["spotify"].getlink2Profile())

    def openTelegram(self):
        self.opensite(self.socials["telegram"].getlink2Profile())

    def openTiktok(self):
        self.opensite(self.socials["tiktok"].getlink2Profile())

    def openTinder(self):
        self.opensite(self.socials["tinder"].getlink2Profile())

    def openStrava(self):
        self.opensite(self.socials["strava"].getlink2Profile())

    def checkWantedProfiles(self):
        if self.check_facebook.isChecked() :
            self.sherlock.addSearchProfile("facebook")
        if self.check_instagram.isChecked():
            self.sherlock.addSearchProfile("instagram")
        if self.check_reddit.isChecked():
            self.sherlock.addSearchProfile("reddit")
        if self.check_twitch.isChecked():
            self.sherlock.addSearchProfile("twitch")
        if self.check_twitter.isChecked():
            self.sherlock.addSearchProfile("twitter")
        if self.check_google.isChecked():
            self.sherlock.addSearchProfile("google")
        if self.check_skype.isChecked():
            self.sherlock.addSearchProfile("skype")
        if self.check_spotify.isChecked():
            self.sherlock.addSearchProfile("spotify")
        if self.check_telegram.isChecked():
            self.sherlock.addSearchProfile("telegram")
        if self.check_tiktok.isChecked():
            self.sherlock.addSearchProfile("tiktok")
        if self.check_tinder.isChecked():
            self.sherlock.addSearchProfile("tinder")
        if self.check_strava.isChecked():
            self.sherlock.addSearchProfile("strava")

    def setFoundProfileBtns(self):
        if self.socials["facebook"].link2Profile != "" and self.socials["facebook"].httpStatus == "200":
            self.btn_facebook.setEnabled(True)
        if self.socials["reddit"].link2Profile != "" and self.socials["reddit"].httpStatus == "200":
            self.btn_reddit.setEnabled(True)
        if self.socials["twitch"].link2Profile != "" and self.socials["twitch"].httpStatus == "200":
            self.btn_twitch.setEnabled(True)
        if self.socials["twitter"].link2Profile != "" and self.socials["twitter"].httpStatus == "200":
            self.btn_twitter.setEnabled(True)
        if self.socials["google"].link2Profile != "" and self.socials["google"].httpStatus == "200":
            self.btn_google.setEnabled(True)
        if self.socials["skype"].link2Profile != "" and self.socials["skype"].httpStatus == "200":
            self.btn_skype.setEnabled(True)
        if self.socials["spotify"].link2Profile != "" and self.socials["spotify"].httpStatus == "200":
            self.btn_spotify.setEnabled(True)
        if self.socials["telegram"].link2Profile != "" and self.socials["telegram"].httpStatus == "200":
            self.btn_telegram.setEnabled(True)
        if self.socials["tiktok"].link2Profile != "" and self.socials["tiktok"].httpStatus == "200":
            self.btn_tiktok.setEnabled(True)
        if self.socials["tinder"].link2Profile != "" and self.socials["tinder"].httpStatus == "200":
            self.btn_tinder.setEnabled(True)
        if self.socials["strava"].link2Profile != "" and self.socials["strava"].httpStatus == "200":
            self.btn_strava.setEnabled(True)

    def checkUsername(self):
        self.sherlock.addUsername(self.input_name.text())

    def trashBinClear(self):
        # deactivate all buttons
        self.deactivateAllSocialBtns()
        self.deactivateBrokenSocials()

        # reset input objects
        self.deactivateAllInputFields()

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
        with open(self.input_name.text() + ".csv") as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                if row[6] == "response_time_s":
                    continue
                try:
                    self.socials[str(row[1]).lower()].link2Profile = str(row[3])
                    self.socials[str(row[1]).lower()].status = str(row[4])
                    self.socials[str(row[1]).lower()].httpStatus = str(row[5])
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
