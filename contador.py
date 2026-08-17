import json
from datetime import datetime


def cargar_horas():
    try:
        with open("horas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return 0
    except json.decoder.JSONDecodeError:
        return 0

horas_viejas = cargar_horas()

inicio = datetime.now()

resultados = input("Presiona Enter para ver resultados")

fin = datetime.now()
diferencia = fin - inicio
horas_nuevas = diferencia.total_seconds() / 3600
horas_total = horas_viejas + horas_nuevas
minutos = horas_total * 60 
horas = horas_total 


print("Tiempo total:", round(minutos, 2), "minutos", round(horas), "horas")

with open ("horas.json", "w") as archivo:
    json.dump(horas_total, archivo)

cerrar = input("Presiona Enter para cerrar")