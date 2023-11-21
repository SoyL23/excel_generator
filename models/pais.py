from config.db import db

class Pais(db.Model):
    __tablename__ = 'pais'

    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(50), nullable=False)
    pais_description = db.Column(db.String(255))

    def __init__(self, pais, pais_description):
        super().__init__()
        self.pais = pais
        self.pais_description = pais_description