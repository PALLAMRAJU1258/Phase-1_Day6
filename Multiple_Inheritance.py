class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)
class Father:
    fathername=""
    def father(self):
        print(self.fathername)
class Son(Mother,Father):
    def parents(self):
        print("Father :",self.fathername)
        print("Mother :",self.mothername)
son=Son()
son.fathername="Sri Ram"
son.mothername="Sri Devi"
son.parents()
