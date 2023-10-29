from flask import Flask
from routes.user import user
from routes.home import home
from config.db import db
from config.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from flask import send_from_directory
# from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

# Configurar la ruta estática para archivos CSS
@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('css', filename)

# Configurar la ruta estática para archivos de imágenes
@app.route('/img/<path:filename>')
def img(filename):
    return send_from_directory('img', filename)

# Configura la URL de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
# Inicializa SQLAlchemy con tu aplicación Flask
db.init_app(app)
migrate = Migrate(app, db)
#Configura Login Manager


#routes
app.register_blueprint(home)
app.register_blueprint(user)

