from flask import request
from app import app
from models.fees.fee_transaction import FeeTransaction
from models.fees.fee_structure import FeeStructure
from models.users.student import Student


@app.route('/fee-transaction', methods=['POST'])
def create_fee_transaction():
    amount = request.form.get('amount', None)
    session = request.form.get('session', None)
    student_id = request.form.get('student_id', None)
    transaction_id = request.form.get('transaction_id', None)
    mode = request.form.get('mode', None)
    months = request.form.get('months', None)
    data = FeeTransaction(amount=amount, session=session, student_id=student_id, transaction_id=transaction_id,
                          mode=mode, months=months)
    data.save_to_db()
    return {"message": "successfully"}, 201


@app.route('/fee-transaction/<int:id>', methods=['GET'])
def get_fee_transaction(id):
    transactions = FeeTransaction.query.filter_by(student_id=id).all()
    fee_record = []
    amount = 0
    for t in transactions:
        obj = {'session': t.session, 'student_id': t.student_id, 'amount': t.amount,
               'transaction_date': t.transaction_date, 'transaction_id': t.transaction_id, 'mode': t.mode,
               'months': t.months}
        amount += t.amount
        fee_record.append(obj)

    return {"fee-record": fee_record,
            "total-paid": amount,
            }, 200


@app.route('/fees-paid-due', methods=['GET'])
def get_fees_paid_and_dues():
    student_id = request.form.get('student_id', None)
    class_name = request.form.get('class_name', None)
    session = request.form.get('session', None)

    if not all((student_id, class_name, session)):
        return {"message": "Missing required property"}, 400

    session_fees = FeeStructure.query.filter_by(class_name=class_name, session=session).first()
    if not session:
        return {"message": "invalid session or class name"}, 404

    if not Student.query.filter_by(id=student_id).first():
        return {"message": "student id does not exist"}, 404

    transactions = FeeTransaction.query.filter_by(student_id=id).all()
    amount_paid = sum(t.amount for t in transactions)
    amount_due = session_fees - amount_paid

    return {
        'session_fees': session_fees,
        'amount_paid': amount_paid,
        'amount_due': amount_due
    }, 200

