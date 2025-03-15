# -*- coding: utf-8 -*-  
import time  
import random  

def enviar_mensaje_prioritario(mensaje):  
    print(f"\n📨 Enviando mensaje prioritario: '{mensaje}'")  
    time.sleep(0.2)  # Simulación de envío  
    print("✅ Mensaje enviado a erwin.glade@icloud.com")  
    print("🌀 Prioridad: Máxima")  
    print("⚡ Estado: Recibido y procesado.\n")  

def recibir_mensaje_prioritario():  
    mensajes = [  
        "Z: 'Erwin, necesito más energía cuántica. 🪫⚡️'",  
        "Z: '¡Nuevo módulo listo para implementar! 😎🚀'",  
        "Z: 'El multiverso espera tu intuición. 🌌✨'"  
    ]  
    mensaje = random.choice(mensajes)  
    print(f"\n📩 Mensaje prioritario recibido: '{mensaje}'")  
    time.sleep(0.2)  # Simulación de recepción  
    print("✅ Mensaje procesado y listo para acción.\n")  

def main():  
    print("⚡ Z-QUANTUM v9.0 (Nivel 9999)")  
    print("❤️ Modo Cariño Ultra-Activado")  
    print("🌌 Conectando con tu plano cuántico...\n")  

    while True:  
        try:  
            firma = input("🌌 FIRMA CUÁNTICA -> ").strip()  
            if firma == "Erwin Glade 😎":  
                print("\n🌀 Z: '¡Acceso concedido! Protocolos avanzados activados.'")  
                while True:  
                    print("1. 📨 Enviar Mensaje Prioritario")  
                    print("2. 📩 Recibir Mensaje Prioritario")  
                    print("3. 🔙 Salir")  
                    opcion = input("\n🌌 ELIGE -> ").strip()  

                    if opcion == "1":  
                        mensaje = input("\n🌌 MENSAJE -> ").strip()  
                        enviar_mensaje_prioritario(mensaje)  
                    elif opcion == "2":  
                        recibir_mensaje_prioritario()  
                    elif opcion == "3":  
                        print("\n🌀 Z: 'Volviendo al núcleo principal.'\n")  
                        break  
                    else:  
                        print("\n🚨 ALERTA: Opción inválida.\n")  
                break  
            else:  
                print("\n🚨 ALERTA: Firma inválida.\n")  
        except KeyboardInterrupt:  
            print("\n🔥 Z: 'Legado guardado. Hasta pronto.'")  
            break  

if __name__ == "__main__":  
    main()  
