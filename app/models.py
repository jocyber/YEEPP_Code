from app import db

#class for the coding problems
class Problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable = False)
    acceptance = db.Column(db.Float, nullable=False, default='0%')
    difficulty = db.Column(db.String(10), nullable=False)

    #constructor
    def __init__(self, title, difficulty):
        self.title = title
        self.difficulty = difficulty

    #toString method
    def __repr__(self):
        return f"{self.id}, {self.title}, {self.acceptance}, {self.difficulty}" 