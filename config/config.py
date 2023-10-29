#Este archivo configura 2 bases de datos,
#Una corresponde a la base de datos que simula
#La base de datos real de e-service que contendra los datos de los tickets
#La otra corresponde a una base de datos que simula la base de datos propia de la aplicacion,
#Con fin de almacenar los reportes generados.
#El objetivo es que al solicitar un reporte
#Consulte si ya existe uno igual, así evita peticiones a E-service.

SQLALCHEMY_DATABASE_URI = "mysql://root:Admin@localhost/excel_generator"
SQLALCHEMY_TRACK_MODIFICATIONS = False
