from config.db import db
from datetime import datetime
# from werkzeug.security import check_password_hash

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    num_employee = db.Column(db.String(7), unique=True) 
    username = db.Column(db.String(15), unique=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True) 
    password = db.Column(db.String(66))  
    campaign = db.Column(db.String(50))  
    role = db.Column(db.String(50))  
    created_date = db.Column(db.DateTime, default=datetime.now)

    # role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    # role = db.relationship('Role', backref='users')


    def __init__(self, num_employee, username, full_name, email, password, campaign, role):
        self.num_employee = num_employee
        self.username = username
        self.full_name = full_name
        self.email = email
        self.password = password
        self.campaign = campaign
        self.role = role

    # def check_pass(self, password):
    #     return generate_password_hash(self.password, passwords)