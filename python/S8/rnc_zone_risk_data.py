"""
Radius Neighbors Classifier (KNN)
Caso: Clasificación de zonas de riesgo sísmico.
Datos de entrada:
 - latitud: Coordenada geográfica.
 - longitud: Coordenada geográfica.
 - profundidad_sismo: Profundidad en km.
Resultado esperado:
 - Salida binaria: 0 (Bajo riesgo) o 1 (Alto riesgo).
Ejemplo: [1, 0, 1]
"""
import pandas as pd
from sklearn.neighbors import RadiusNeighborsClassifier

cols = [
    "latitude",
    "longitude",
    "depth_earthquake",
]

columns_renamed = {
    "Latitud": "latitude",
    "Longitud": "longitude",
    "Profundidad del sismo": "depth_earthquake"
}

def get_data_from_file(filename: str):
    if filename.endswith(".csv"):
        transport_package_data = pd.read_csv(
            f"./static/files/upload/{filename}",
            sep=";",
        )
    else:
        transport_package_data = pd.read_excel(
            f"./static/files/upload/{filename}",
        )

    return transport_package_data

def get_path_file(filename: str, transport_package_data: pd.DataFrame):
    path_file = (f"./static/files/downloads/Resultado_{filename}").replace(" ", "_")

    if filename.endswith(".csv"):
        transport_package_data.to_csv(
            path_file,
            index=False,
            sep=";",
        )
    else:
        transport_package_data.to_excel(
            path_file,
            index=False,
        )

    return path_file

def train_risk_data(zone_data_length: int) -> RadiusNeighborsClassifier:
    zone_risk_data = pd.DataFrame({
        "latitude": [19.4326, 34.0522, 51.5074],
        "longitude": [-99.1332, -118.2437, -0.1278],
        "depth_earthquake": [20, 10, 30],
        "risk_level": [0, 1, 0]
    })

    print(f"zone_data_length => {zone_data_length}")

    neigh = RadiusNeighborsClassifier(radius=zone_data_length, outlier_label = 0)
    x = zone_risk_data[cols]
    y = zone_risk_data["risk_level"]

    neigh.fit(x, y)

    return neigh

def get_predict_data_from_file(filename: str):
    zone_data = get_data_from_file(filename)

    zone_data.rename(
        columns = columns_renamed,
        inplace = True,
    )

    if zone_data['latitude'].dtype == 'O':
        zone_data['latitude'] = zone_data['latitude'].str.replace(',', '.').astype(float)
    if zone_data['longitude'].dtype == 'O':
        zone_data['longitude'] = zone_data['longitude'].str.replace(',', '.').astype(float)

    model = train_risk_data(zone_data.shape[0])

    zone_risk_data = zone_data[cols].copy()
    zone_risk_data["risk_level"] = model.predict(zone_data[cols])

    zone_risk_data.loc[zone_risk_data["risk_level"] == 1, "risk_level"] = "Alto riesgo"
    zone_risk_data.loc[zone_risk_data["risk_level"] == 0, "risk_level"] = "Bajo Riesgo"

    zone_risk_data['latitude'] = zone_risk_data['latitude'].astype(str).str.replace('.', ',')
    zone_risk_data['longitude'] = zone_risk_data['longitude'].astype(str).str.replace('.', ',')

    columns_name = { item: keys for keys, item in columns_renamed.items() }
    zone_risk_data_original = zone_risk_data.to_dict(orient="records")
    zone_risk_data.rename(
        columns = {
            **columns_name,
            "risk_level": "Nivel del riesgo",
        },
        inplace = True,
    )

    return {
        "zone_risk_data": zone_risk_data_original,
        "path_file": get_path_file(filename, zone_risk_data)
    }

def get_template_file_path():
    template = pd.DataFrame({
        "Latitud": ['19,4326', '34,0522', '51,5074'],
        "Longitud": ['-99,1332', '-118,2437', '-0,1278'],
        "Profundidad del sismo": [20, 10, 30],
    })

    template_file_path = "./static/files/origin/plantilla_zonas_sismos.csv"

    template.to_csv(
        template_file_path,
        index=False,
        sep=";",
    )

    return template_file_path
