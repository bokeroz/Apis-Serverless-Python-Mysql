import mysql.connector
import json
import os

def main(event, context):
    #event = {"estatus":"vendido", "ano":"2000", "cuidad":"bogota"} #JSON
    #Obtener variables de ambiente     
    e = dict(os.environ.items())
    
    #sentencia para validar si trae algun valor para filtrar 
    if not event['estatus']:
        #estatus de propiedad por default
        event['estatus'] = "in ('pre_venta','pre_venta', 'vendido')"
        query = '''SELECT habi_db.property.address as Direccion, habi_db.property.city as Ciudad, habi_db.property.price as Precio_de_venta, habi_db.property.description as Descripcion FROM habi_db.property INNER JOIN habi_db.status ON habi_db.property.id = habi_db.status.id where habi_db.status.name %s '''%(event['estatus'])
    else: 
        query = '''SELECT habi_db.property.address as Direccion, habi_db.property.city as Ciudad, habi_db.property.price as Precio_de_venta, habi_db.property.description as Descripcion FROM habi_db.property INNER JOIN habi_db.status ON habi_db.property.id = habi_db.status.id where habi_db.status.name = "%s" '''%(event['estatus'])
    #sentencia para validar si trae algun valor para filtrar 
    if event['ano']:
        query = query + '''AND year = "%s"'''%(event['ano'])
    #sentencia para validar si trae algun valor para filtrar 
    if event['cuidad']:
        query = query + '''AND city = "%s"'''%(event['cuidad']) 
    print(query)        
    try:
        #conecion a base de datos 
        connection = mysql.connector.connect(user=e['USER'], password=e['PASSWORD'], host=e['HOST'], database=e['DATABASE'], port=e['PORT'])                
        cursor = connection.cursor()
        #ejecucion de consulta 
        cursor.execute( query )
        data = cursor.fetchall()
        print(data)

    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        return {
            "statusCode": 500,
            "body": {"error":"Internal Server problem during the execution"}
        }

    response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }

    return response

if __name__ == "__main__":
    main('', '')