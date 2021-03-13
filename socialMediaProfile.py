

class socialMediaProfile:

    username = ""
    webAddr = ""

    def __init__(self, web):
        self.setWebAddr(web)

    def setUsername(self, usr):
        self.username = usr

    def setWebAddr(self, web):
        self.webAddr = web

    def getlink2Profile(self):
        return self.webAddr + self.username

