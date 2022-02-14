from app import db

#class for the coding problems
class Problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)#artificial key
    title = db.Column(db.String(50), nullable = False)
    acceptance = db.Column(db.Float, nullable=False, default=0.0)
    difficulty = db.Column(db.String(10), nullable=False)

    #toString method
    def __repr__(self):
        return f"{self.id}, {self.title}, {self.acceptance}, {self.difficulty}" 

