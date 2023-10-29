from flask import Blueprint

ticket = Blueprint('ticket', __name__)

@ticket.route('ticket/get')
def get_tickets():
    pass