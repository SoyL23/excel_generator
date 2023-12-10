from flask import Blueprint, request, render_template

report = Blueprint('report', __name__)

@report.route('report/create', methods=['GET', 'POST'])
def create_report():
    if request.method == 'GET':
        return render_template('')
    else:
        pass
    pass

@report.route('report/edit', methods=['GET', 'POST'])
def edit_report():
    if request.method == 'GET':
        return render_template('')
    else:
        pass
    

@report.route('report/get', methods=['GET', 'POST'])
def get_report():
    if request.method == 'GET':
        return render_template('')
    else:
        pass
    

@report.route('report/delete', methods=['GET', 'POST'])
def delete_report():
    if request.method == 'GET':
        return render_template('')
    else:
        pass
    pass


@report.route('/route_name', methods=['GET', 'POST'] )
def method_name():
    pass