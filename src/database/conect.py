import pymysql as MySql

def try_conect():
    conect = MySql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Admin",
        database="excel_generator"
    )
    try:  
        with conect.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            
            # result = cursor.fetchone()
            # print("Conectado a la base de datos:", result[0])
    except Exception as e:
        print("Ha ocurrido un error", e)
        
    finally:
        conect.close()