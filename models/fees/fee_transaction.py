from app import db
from datetime import datetime
from enum import Enum

class PaymentMode(str, Enum):
    NET_BANKING = 'NET_BANKING'
    DEBIT_CARD = 'DEBIT_CARD'
    CREDIT_CARD = 'CREDIT_CARD'
    OFFLINE = 'OFFLINE'


class FeeTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), index=True, nullable=False)
    amount = db.Column(db.Integer, nullable=True)
    session = db.Column(db.String(10), nullable=False)
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    transaction_id = db.Column(db.String(255), nullable=False)
    mode = db.Column(db.Enum(PaymentMode), nullable=False)
    months = db.Column(db.String(64), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

