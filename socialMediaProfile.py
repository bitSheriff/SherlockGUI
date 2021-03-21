

class socialMediaProfile:

    username = ""
    sherlockID = ""
    status = ""
    link2Profile = ""
    httpStatus = "0"

    def __init__(self, id):
        self.sherlockID = id

    def setUsername(self, usr):
        self.username = usr

    def getlink2Profile(self):
        return self.link2Profile

