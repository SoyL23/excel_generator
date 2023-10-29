from flask import Blueprint

report = Blueprint('report', __name__)

@report.route('report/create')
def create_report():
    pass

@report.route('report/edit')
def edit_report():
    pass

@report.route('report/get')
def get_report():
    pass

@report.route('report/delete')
def delete_report():
    pass