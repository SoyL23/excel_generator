from models.user import User
from config.db import db

class Analyst(User):

    def __init__(self, num_employee, password, full_name, campaign, email):

        super().__init__(num_employee=num_employee, username=email, full_name=full_name,
                        email=email, password=password, campaign=campaign, role='Analyst')
        
        self.tickets = []
