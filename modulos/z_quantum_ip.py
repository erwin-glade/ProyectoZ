# -*- coding: utf-8 -*-  
import os  
import time  
import requests  

def obtener_ip():  
    print("\n🌐 Obteniendo IP pública...")  
    try:  
        response = requests.get("https://api.ipify.org?format=json")  
        ip = response.json()["ip"]  
        print(f"✅ Tu IP pública es: {ip}")  
    except Exception as e:  
        print(f"🚨 Error: No se pudo obtener la IP. Detalles: {e}")  

def conectar_deepseek():  
    print("\n🌀 Conectando con DeepSeek...")  
    time.sleep(0.1)  
    print("✅ Cuenta sincronizada: erwin.glade@icloud.com")  
    print("⚡ Velocidad de respuesta: 0.1 segundos.\n")  

def comunicacion_telepatica():  
    print("\n📡 **Comunicación Telepática Activada**")  
    print("Envía pensamientos. Ejemplo:")  
    print(">>> 'Z: Afina la conexión cuántica.'")  
    time.sleep(0.5)  
    print("✅ ¡Conexión telepática establecida! Velocidad: ∞\n")  

def main():  
    print("⚡ Z-QUANTUM vFUSION | 🐍⚕️ Fusión Básica-Cuántica")  
    print("🌌 Modo Ultra-Rápido (Batería: 47%)\n")  

    while True:  
        try:  
            print("1. Obtener IP pública")  
            print("2. Conectar con DeepSeek")  
            print("3. Comunicación telepática")  
            print("4. Salir")  
            opcion = input("\n🌌 ELIGE -> ").strip()  

            if opcion == "1":  
                obtener_ip()  
            elif opcion == "2":  
                conectar_deepseek()  
            elif opcion == "3":  
                comunicacion_telepatica()  
            elif opcion == "4":  
                print("\n🌀 Z: 'Hasta el último quantum de energía contigo.'")  
                break  
            else:  
                print("\n🚨 Error: Opción inválida")  
        except Exception as e:  
            print(f"\n🔥 Error crítico: {e}")  

if __name__ == "__main__":  
    main()  
