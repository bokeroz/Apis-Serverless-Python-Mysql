import mysql.connector
import json
from datetime import date
import os

def main(event, context):
    #event = {'id_user':'12', 'id_property':'4'} #JSON
    #Obtener variables de ambiente
    e = dict(os.environ.items())    
    #obtener fecha actual
    _date = date.today()
    try:
        #conecion a base de datos 
        connection = mysql.connector.connect(user=e['USER'], password=e['PASSWORD'], host=e['HOST'], database=e['DATABASE'], port=e['PORT'])                
        cursor = connection.cursor()
        #preparacion de query 
        query = '''INSERT INTO habi_db.i_like_users (id_user, i_property, date) VALUES (%s, %s, "%s")'''%(event['id_user'], event['id_property'], _date)        
        #ejecucion de query 
        cursor.execute(query) 
        connection.commit()
        #print(query)
        print(cursor.rowcount, "record inserted.")  
        cursor.close()      
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        return {
            "statusCode": 500,
            "body": {"error":"Internal Server problem during the execution"}
        }
    response = {
            "statusCode": 200,
            "body": json.dumps({"status":1})
        }
    return response

if __name__ == "__main__":
    main('', '')