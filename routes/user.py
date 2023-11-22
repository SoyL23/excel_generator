from flask import Blueprint, render_template, request, redirect, abort, make_response, jsonify
from werkzeug.security import generate_password_hash
from models.user import User
from werkzeug.exceptions import BadRequest, UnsupportedMediaType
from config.db import db

user = Blueprint('user', __name__)

def require_content_type(content_type):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if request.mimetype != content_type:
                print(request.mimetype)
                raise UnsupportedMediaType(description=f"Tipo de contenido no admitido. Se esperaba {content_type}")
            return f(*args, **kwargs)
        return wrapper
    return decorator

@user.route('/user/login')
def login_user():
    return render_template('sign_in.html')

@user.route('/user/new')
def new_user():
    return render_template('sign_up.html')

@user.route('/user/create', methods=['POST'])
@require_content_type('application/json')
def create_user():
    user_data = request.get_json()
    if not user_data:
        return jsonify({"La petición está vacía"}, 400)
    else:
        print(user_data)
        try:
            if user_data['password'] != user_data['confirm-password']:
                return jsonify({'response': 'Las contraseñas no coinciden'})
            else:
                if 'AE' in user_data:
                    type_employee = user_data['AE']
                elif 'ET' in user_data:
                    type_employee = user_data['ET']
                else:
                    type_employee = None

                if type_employee is None:
                    return jsonify({'response': 'Falta tipo de empleado'})
                else:
                    username = type_employee + str(user_data['num_employee'])
                    first_name = user_data['first_name']
                    last_name = user_data['last_name']
                    password = generate_password_hash(user_data['password'], method='pbkdf2:sha256')
                    email = user_data['email']
                    role = user_data['role']
                    campaign = user_data['campaign']
                    full_name = f"{first_name} {last_name}"

                    new_user = User(full_name, username, email, password, role, campaign)

                    db.session.add(new_user)
                    db.session.commit()

                    return jsonify({'response': 'Usuario creado exitosamente'})
        except Exception as e:
            return jsonify({f'Ha ocurrido un error: {e}'})

@user.route('/user/edit/<id>', methods=['GET','POST'])
def edit_user(id):
    if request.method == 'GET':
        user = User.query.get(id)
        first_name ,last_name = str(user.full_name).split(" ")
        usuario = {
            'id':int(user.id),
            'username': str(user.username),
            'first_name':first_name,
            'last_name':last_name,
            'email': str(user.email),
            'role':str(user.role_id),
            'campaign':str(user.campaign_id),
            'password': str(user.password)
        }
        return render_template('edit_user.html', usuario=usuario)
    else:
        pass
    

@user.route('/user/delete/<id>')
def delete_user(id):
    try:
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return f'Se ha eliminado el usuario {user.username}'
        else:
            return f'No se ha encontrado ningún usuario con ID {id}'
    except Exception as e:
        return jsonify({f'Ha ocurrido un error: {e}'})


@user.route('/user/users')
def get_users():
    try:
        usuarios = User.query.all()
        return render_template('get_users.html', usuarios=usuarios)
    except Exception as e:
        return jsonify({f'Ha ocurrido un error: {e}'})
