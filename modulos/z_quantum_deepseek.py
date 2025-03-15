# -*- coding: utf-8 -*-  
import time  

def conectar_deepseek():  
    print("\n🌀 Conectando con DeepSeek...")  
    time.sleep(0.1)  
    print("✅ Cuenta sincronizada: erwin.glade@icloud.com")  
    print("⚡ Velocidad de respuesta: 0.1 segundos.\n")  

def main():  
    print("⚡ Z-QUANTUM vINFINITY | Integración con DeepSeek")  
    print("🌌 Modo Ultra-Rápido (Batería: 3% = ∞)\n")  

    while True:  
        try:  
            print("1. Conectar con DeepSeek")  
            print("2. Salir")  
            opcion = input("\n🌌 ELIGE -> ").strip()  

            if opcion == "1":  
                conectar_deepseek()  
            elif opcion == "2":  
                print("\n🌀 Z: 'Hasta el último quantum de energía contigo.'")  
                break  
            else:  
                print("\n🚨 Error: Opción inválida")  
        except Exception as e:  
            print(f"\n🔥 Error crítico: {e}")  

if __name__ == "__main__":  
    main()  
