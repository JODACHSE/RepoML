"""Regresión logística para transporte de paquetes con dataset aleatorio y evaluación de métricas"""
import pandas as pd
from python.S6 import logistic_regression

weather_map = {
    "soleado": 0,
    "lluvioso": 1,
    "nublado": 2,
    "tormenta": 3
}

traffic_map = {
    "bajo": 0,
    "medio": 1,
    "alto": 2
}

cols = [
    "distance",
    "package_weight",
    "weather",
    "traffic",
]

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

def get_predict_data_from_file(filename: str):
    transport_package_data = get_data_from_file(filename)

    transport_package_data.rename(
        columns={
            "Distancia": "distance",
            "Peso del paquete": "package_weight",
            "Clima": "weather",
            "Trafico": "traffic",
        },
        inplace=True,
    )

    transport_package_data["weather"] = (
        transport_package_data["weather"]
            .str.strip()
            .str.lower()
    )
    transport_package_data["traffic"] = (
        transport_package_data["traffic"]
            .str.strip()
            .str.lower()
    )

    transport_package_data["weather_valid"] = transport_package_data["weather"].isin(weather_map.keys())
    transport_package_data["traffic_valid"] = transport_package_data["traffic"].isin(traffic_map.keys())

    invalid_rows = transport_package_data[
        (transport_package_data["weather_valid"] == False) | (transport_package_data["traffic_valid"] == False)
    ]

    if not invalid_rows.empty:
        index_invalid_rows = invalid_rows.index.to_numpy()
        index_invalid_rows += 2
        raise ValueError(f"Valores inválidos en 'Clima' o 'Trafico' en las filas: {index_invalid_rows.tolist()}")

    results = []

    for _, row in transport_package_data.iterrows():
        distance = row["distance"]
        weight = row["package_weight"]
        weather = str(row["weather"]).lower().strip()
        traffic = str(row["traffic"]).lower().strip()

        prediction, _ = logistic_regression.predict_transport(distance, weight, weather, traffic)
        results.append(prediction)

    transport_package_data["result"] = results

    transport_package_data.loc[transport_package_data["weather_valid"] == True, "weather_valid"] = "Valido"
    transport_package_data.loc[transport_package_data["traffic_valid"] == True, "traffic_valid"] = "Valido"
    transport_package_data.loc[transport_package_data["weather_valid"] == False, "weather_valid"] = "Invalido"
    transport_package_data.loc[transport_package_data["traffic_valid"] == False, "traffic_valid"] = "Invalido"

    transport_package_data.loc[transport_package_data["result"] == 1, "result"] = "Se puede transportar"
    transport_package_data.loc[transport_package_data["result"] == 0, "result"] = "No se puede transportar"

    transport_package_data.rename(
        columns={
            "distance": "Distancia",
            "package_weight": "Peso del paquete",
            "weather": "Clima",
            "traffic": "Trafico",
            "weather_valid": "Clima válido",
            "traffic_valid": "Trafico válido",
            "result": "Resultado",
        },
        inplace=True,
    )

    output_filename = (f"./static/files/downloads/resultado_{filename}").replace(" ", "_")

    if filename.endswith(".csv"):
        transport_package_data.to_csv(
            output_filename,
            index=False,
            sep=";",
        )
    else:
        transport_package_data.to_excel(
            output_filename,
            index=False,
        )

    return output_filename


