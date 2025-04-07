from python.db_connection import mySql

def get_models_data():
    cursor = mySql.connection.cursor()
    query = """
        SELECT
            i.id_Imagen,
            i.link_Imagen,
            c.Descripcion AS caracteristica,
            c.Referencia AS referencia,
            m.Nombre_Modelo AS modelo
        FROM
            imagenes i
        JOIN
            caracateristicas c ON i.id_Modelo = c.id_Modelo
        JOIN
            modelos m ON i.id_Modelo = m.id_Modelo;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data