from config.db import db
from models.role import Role
from models.campaign import Campaign
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(66))

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref='users')

    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    campaign = db.relationship('Campaign', backref='campaigns')

    created_date = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, full_name, username, email, password, role_id, campaign_id):
        super().__init__()
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = password
        self.role_id = role_id
        self.campaign_id = campaign_id

    def __repr__(self):
        return f'<User {self.username}>'
