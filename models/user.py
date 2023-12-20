from config.db import db
from models.role import Role
from models.campaign import Campaign
from datetime import datetime
from werkzeug.security import check_password_hash
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128))

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref='users')
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    campaign = db.relationship('Campaign', backref='users')

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
    
    def to_dict(self):
        role = self.role.to_dict()
        campaign = self.campaign.to_dict()
        return {
            
            "id": self.id,
            "full_name": self.full_name,
            "username": self.username,
            "email": self.email,
            "role_id": self.role_id,
            "role": role['role'],
            "campaign_id": self.campaign_id,
            "campaign":campaign,
            "created_date": self.created_date
        }
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)
