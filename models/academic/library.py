from app import db

class Library(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, default=0, nullable=False)
