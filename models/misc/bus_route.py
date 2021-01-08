from app import db

class BusRoute(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bus_id = db.Column(db.Integer, index=True, nullable=False)
    route = db.Column(db.String(128), nullable=False)
    time = db.Column(db.Time, nullable=False)

