from flask import Flask, send_from_directory
from config.db import db
from config.config import Config_Development
from routes.user import user
from routes.home import home
from sqlalchemy import create_engine
from flask_migrate import Migrate
from flask.json import jsonify

app = Flask(__name__)

app.config.from_object(Config_Development)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Configurar la ruta estática para archivos CSS
@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('css', filename)

# Configurar la ruta estática para archivos de imágenes
@app.route('/img/<path:filename>')
def img(filename):
    return send_from_directory('img', filename)

@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory('js', filename)

# Inicializa SQLAlchemy con tu aplicación Flask
db.init_app(app)
migrate = Migrate(app, db)

#routes
app.register_blueprint(home)
app.register_blueprint(user)

