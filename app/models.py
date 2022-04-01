
#class for the coding problems
class Problems():

    def __init__(self,data):
        self.id = data[0]
        self.title = data[4]
        self.acceptance = data[2]
        self.difficulty = data[1]

    def get_title(self):
        return self.title

    def get_acceptance(self):
        return self.acceptance

    def get_difficulty(self):
        return self.difficulty