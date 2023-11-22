from app import app
from config.db import db


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()

"""
Aplicación web capaz de generar reportes en excel con datos de una base de datos
y almacenarlos en otra, con el objetivo de automatizar el proceso de llenado de exceles por parte
de los Agentes del area de UP

Ultima actualización: 21 - Nov - 2023
Todas las librerias utilizadas en el back-end estan en el archivo requirements.txt
Desarrollado por: https://github.com/SoyL23
"""