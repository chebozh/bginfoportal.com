from BGInfoPortal import db


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    url = db.Column(db.String(50))
    category = db.Column(db.String(20))
    site_base_url = db.Column(db.String(20))
    date_added = db.Column(db.Integer)

    def __repr__(self):
        return f'Article: {self.title}, {self.url}'
