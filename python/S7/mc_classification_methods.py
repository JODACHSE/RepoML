from python.db_connection import mySql

def get_models_data():
    cursor = mySql.connection.cursor()
    query = """
        SELECT
            i.id_Imagen,
            i.link_Imagen,
            c.Descripcion AS caracteristica,
            c.Referencia AS referencia,
            m.id_Modelo,
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

    # Agrupar datos por id_Modelo
    grouped_data = {}
    for row in data:
        model_id = row['id_Modelo']
        if model_id not in grouped_data:
            grouped_data[model_id] = {
                "nombre_modelo": row['modelo'],
                "imagenes": []
            }
        grouped_data[model_id]["imagenes"].append(row)
    
    return grouped_data