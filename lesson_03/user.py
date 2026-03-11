class User:

    def __init__(self, name):
        self.userName = name,

    def sayFstName(self):
        print("Имя ", self.FstName)

    def setFstName(self, newFstName):
        self.FstName = newFstName

    def sayLstName(self):
        print("Фамилия ", self.LstName)

    def setLstName(self, newLstName):
        self.LstName = newLstName

    def sayFlName(self):
        print("Имя и Фамилия ", self.FstName, self.LstName)