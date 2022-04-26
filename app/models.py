#class for the coding problems
class Problems():
    def __init__(self,data=[0,1,2,3,4,5,112,3]):
        self.id = data[0]
        self.title = data[4]
        try:
            self.acceptance = data[3] / data[2] * 100
        except:
            self.acceptance = 0
        self.difficulty = data[1]
        self.likes = data[6]
        self.dislikes = data[7]

    def get_title(self):
        return self.title

    def get_acceptance(self):
        return self.acceptance

    def get_difficulty(self):
        return self.difficulty

    def get_id_path(self):
        return f"test?id={self.id}"

class Problem_Info():
    def __init__(self,data=[1 for x in range(1,10000)]):
        self.id = data[0]
        self.title = data[4]
        self.description = data[5]
        self.likes = data[6]
        self.dislikes = data[7]
        self.input = data[10]
        self.output = data[11]
        self.methodHeader = data[-1]

class User():
    def __init__(self,data=[1 for x in range(1,10000)]):
        self.user_id = data[0]
        self.full_name = data[1]
        self.username = data[5]
        self.email = data[6]
