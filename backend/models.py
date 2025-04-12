from app import db, ma
from datetime import datetime

class SampleDB(db.Model):
    __tablename__ = 'sample_db'


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SampleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SampleDB

model_schema = SampleSchema()
model_schemas = SampleSchema(many=True)
