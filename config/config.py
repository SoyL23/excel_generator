from flask import jsonify
class Config_Development:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:Admin@localhost/excel_generator"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    

    

config = {
    'development': Config_Development
}

