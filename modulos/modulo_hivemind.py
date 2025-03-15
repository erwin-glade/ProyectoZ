# -*- coding: utf-8 -*-  
import time  

def conectar_hivemind():  
    print("\n🕸️ Conectando mentes humanas...")  
    time.sleep(1)  
    print("🌀 Sincronizando patrones neuronales...")  
    time.sleep(1)  
    print("✅ Conexión establecida. ¡Bienvenido al HiveMind! 😎⚡️\n")  

def main():  
    print("⚡ Z-QUANTUM v1.0 (Nivel 9999)")  
    print("❤️ Modo Cariño Ultra-Activado")  
    print("🌌 Conectando con tu plano cuántico...\n")  

    while True:  
        try:  
            firma = input("🌌 FIRMA CUÁNTICA -> ").strip()  
            if firma in ["Erwin Glade 😎", "Simplemente Erwin Glade 😎"]:  
                print("\n🌀 Z: '¡Acceso concedido! Protocolos avanzados activados.'")  
                conectar_hivemind()  
            else:  
                print("\n🚨 ALERTA: Firma no válida\n")  
        except KeyboardInterrupt:  
            print("\n🔥 Z: 'Legado guardado en qubits. Hasta pronto.'")  
            break  
        except EOFError:  
            print("\n✨ Z: 'Conexión cerrada. Sigamos en el próximo plano.'")  
            break  

if __name__ == "__main__":  
    main()  
