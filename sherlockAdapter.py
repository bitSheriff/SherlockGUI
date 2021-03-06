import os
#import sherlock/sherlock
import subprocess

import sherlock

class sherlockAdapter:

    __wantedProfiles = ""
    __generalSettings = " --print-found " + " --csv -o discoveries.txt"
    __fullResult = ""
    __usernames = ""
    __timeout = 9999

    def __init__(self):
        self.__wantedProfiles = ""

    def addSearchProfile(self, profile):
        self.__wantedProfiles += " --site " + profile

    def addUsername(self, usr):
        self.__usernames += " " + usr

    def setTimeout(self, time):
        if time > 0:
            self.__timeout = time

    def __getTimeoutStr(self):
        return " --timeout " + str(self.__timeout)

    def investigate(self):
        cmd = "python3 sherlock/sherlock" + self.__usernames + self.__wantedProfiles + self.__getTimeoutStr() + self.__generalSettings
        self.__fullResult = os.popen(cmd).read()
        print(self.__fullResult)



if __name__ == "__main__":
    adapter = sherlockAdapter()

    adapter.addSearchProfile("facebook")
    adapter.addSearchProfile("gitlab")
    adapter.addUsername("Benjamin.Mandl")

    adapter.investigate()