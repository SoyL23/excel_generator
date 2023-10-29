from config.db import db
from datetime import datetime

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    works_employees = db.Column(db.String(255))
    application = db.Column(db.String(255))
    assignee_to = db.Column(db.String(50))
    start_date = db.Column(db.DateTime)
    comp_date = db.Column(db.DateTime)

    created_date = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, isar_number, works_employees, application, assignee_to, start_date, comp_date):
        self.id = isar_number
        self.works_employees = works_employees
        self.application = application
        self.assignee_to = assignee_to
        self.start_date = start_date
        self.comp_date = comp_date
