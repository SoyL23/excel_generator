from flask import sessions, session, request

def auth_user():
    data = request.form.items
    print (type(data))
    pass
auth_user()