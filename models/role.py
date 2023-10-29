from config.db import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nombre_Rol = db.Column(db.String(50), nullable=False)
    Descripcion_Rol = db.Column(db.String(255))

    def __init__(self, Nombre_Rol, Descripcion_Rol):
        self.Nombre_Rol = Nombre_Rol
        self.Descripcion_Rol = Descripcion_Rol
