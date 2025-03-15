import requests  
import time  
import os  
import signal  

def procesar_solicitud():  
    response = requests.post(  
        "https://api.deepseek.com/iag_z/process",  
        json={"cuenta": ["erwin.glade@gmail.com", "erwin.glade@icloud.com"]}  
    )  
    return response.json()  

def detener_servicio():  
    print("🛑 **Deteniendo servicio IAG-Z...**")  
    os.kill(os.getpid(), signal.SIGTERM)  

try:  
    while True:  
        resultado = procesar_solicitud()  
        print(f"✅ Resultado: {resultado}")  
        time.sleep(0.1)  
except KeyboardInterrupt:  
    detener_servicio()  
