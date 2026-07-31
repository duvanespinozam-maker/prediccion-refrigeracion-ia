import requests
import random
import time
from datetime import datetime

URL = "https://script.google.com/macros/s/AKfycbxe5ZJfUPvzVbQwtn3pihUgDyVb0VHGvn_3OWIL91pFha0hEM62RZRxbuKzF5X0DpJL/exec"

reporte = 1

while True:

    temperatura = round(random.uniform(30, 65), 1)
    humedad = round(random.uniform(45, 60), 1)
    corriente = round(random.uniform(6, 15), 2)
    vibracion = round(random.uniform(0.8, 4.5), 2)
    presion = round(random.uniform(90, 180), 1)
    horas = random.randint(500, 6000)

    if temperatura >= 56:
        estado = "FALLA CRITICA"
        riesgo = "ALTO"
        probabilidad = 98
        falla = "SOBRECALENTAMIENTO DEL COMPRESOR"
        accion = "DETENER EQUIPO"
        procedimiento = "REVISAR COMPRESOR Y CONDENSADOR"
        tiempo = "INMEDIATO"
        prioridad = "ALTA"

    elif temperatura >= 46:
        estado = "ALERTA"
        riesgo = "MEDIO"
        probabilidad = 70
        falla = "CONDENSADOR SUCIO"
        accion = "PROGRAMAR MANTENIMIENTO"
        procedimiento = "LIMPIAR CONDENSADOR"
        tiempo = "24 HORAS"
        prioridad = "MEDIA"

    else:
        estado = "NORMAL"
        riesgo = "BAJO"
        probabilidad = 5
        falla = "NINGUNA"
        accion = "CONTINUAR OPERACIÓN"
        procedimiento = "NO REQUIERE"
        tiempo = "30 DIAS"
        prioridad = "BAJA"

    ahora = datetime.now()

    datos = {
        "fecha": ahora.strftime("%Y-%m-%d"),
        "hora": ahora.strftime("%H:%M:%S"),
        "reporte": reporte,
        "temperatura": temperatura,
        "humedad": humedad,
        "corriente": corriente,
        "vibracion": vibracion,
        "presion": presion,
        "horas": horas,
        "estado": estado,
        "riesgo": riesgo,
        "probabilidad": probabilidad,
        "falla": falla,
        "accion": accion,
        "procedimiento": procedimiento,
        "tiempo": tiempo,
        "prioridad": prioridad
    }

    try:
        requests.post(URL, json=datos, timeout=10)
        print("Registro enviado:", reporte)
    except Exception as e:
        print("Error:", e)

    reporte += 1

    time.sleep(900)
