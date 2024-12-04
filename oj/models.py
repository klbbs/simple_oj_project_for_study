from oj import db
from sqlalchemy import func

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(10), nullable=False)
    input_sample = db.Column(db.Text, nullable=False)
    output_sample = db.Column(db.Text, nullable=False)
    
    __table_args__ = (
        db.Index('idx_category','category'),
        db.Index('idx_difficulty','difficulty'),
        db.Index('idx_title','title'),
    )


class Submit(db.Model):
    __tablename__ = 'submit'
    text = db.Column(db.Text, nullable=False)
    sub_id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, default=func.utcnow(), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    author = db.relationship('User',back_populates='submits')


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    submits = db.relationship('Submit',back_populates='author',cascade='all, delete-orphan')
