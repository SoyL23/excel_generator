from models.user import User
from flask import session, request, render_template, jsonify, Blueprint, redirect
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/auth/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        return render_template('sign_in.html')
    else:
        try:
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user is None:
                return jsonify({'No existe este usuario'})
            else:
                if user.check_password(user.password, password):
                    role = user.role.to_dict()
                    session['status'] = True
                    session['fullname'] = user.full_name
                    session['username'] = user.username
                    session['role'] = role
                    session['campaign'] = user.campaign.to_dict()
                    return f'Logueado {session["username"]}' #render_template('')
                else:
                    return jsonify({'Invalid Password'})
        except Exception as ex:
            return f'Ha ocurrido un error: {ex}'

@auth.route('/auth/logout')
def logout_user():
    session.clear()
    return redirect('/')

def check_inactivity():
    now = datetime.now()
    last_activity = session.get('last_activity')
    if last_activity is not None and (now - last_activity).total_seconds() > 600:
        session.clear()