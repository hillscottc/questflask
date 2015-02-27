from app import db
from sqlalchemy.dialects.postgresql import JSON


class Clue(db.Model):
    __tablename__ = 'questapp_clue'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String())
    question = db.Column(db.String())
    answer = db.Column(db.String())

    def __init__(self, category, question, answer):
        self.category = category
        self.question = question
        self.answer = answer

    def __repr__(self):
        return '<id {}>'.format(self.id)

