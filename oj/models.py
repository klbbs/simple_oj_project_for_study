from oj import db


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