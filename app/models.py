from app import db

class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    style = db.Column(db.String(100), nullable=True)
    year = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Artwork {self.title}>'