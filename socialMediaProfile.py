

class socialMediaProfile:

    username = ""
    webAddr = ""
    sherlockID = ""
    status = ""
    link2Profile =""

    def __init__(self, web, id):
        self.setWebAddr(web)
        self.sherlockID = id

    def setUsername(self, usr):
        self.username = usr

    def setWebAddr(self, web):
        self.webAddr = web

    def getlink2Profile(self):
        return self.link2Profile

