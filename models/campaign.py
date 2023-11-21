from config.db import db
from models.pais import Pais


class Campaign(db.Model):
    __tablename__ = 'campaign'

    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(50), nullable=False)
    campaign_description = db.Column(db.String(255))
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'))

    # Define la relación con la clase 'Pais'
    pais = db.relationship('Pais', backref='paises')

    def __init__(self, campaign_name, campaign_description, pais_id=None):
        super().__init()
        self.campaign_name = campaign_name
        self.campaign_description = campaign_description
        self.pais_id = pais_id

