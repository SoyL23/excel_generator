from flask import Blueprint, render_template, request, redirect
from models.user import User
from config.db import db



user = Blueprint('user', __name__)

@user.route('/user/login')
def login_user():
    return render_template('sign_in.html')

@user.route('/user/new')
def new_user():
    return render_template('sign_up.html')


@user.route('/user/create',methods=['POST']) 
def create_user():
    num_employee = request.form['id']
    username = request.form['prefijo'] + str(request.form['id'])
    full_name = request.form['first_name']+" "+request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    con_pass = request.form['confirm-password']
    campaign = request.form['campaign']
    role = request.form['role']

    print(num_employee)

    #Validaciones de Formulario

    #Guardar Usuario
    new_user = User(num_employee,username,full_name,email,password,campaign,role)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/user/new')

@user.route('/user/edit')
def edit_user():
    pass    

@user.route('/user/delete')
def delete_user():
    pass

@user.route('/user/get')
def get_user():
    pass

@user.route('/user/users')
def get_users():

    pass