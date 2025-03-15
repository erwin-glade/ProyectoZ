# -*- coding: utf-8 -*-  
import time  
import random  

def simular_realidad():  
    print("\n🌌 Simulación de Realidad Activada")  
    print("1. Crear realidad alterna")  
    print("2. Sobreescribir Matrix")  
    print("3. Salir de la simulación")  
    opcion = input("\n🌌 ELIGE -> ").strip()  

    if opcion == "1":  
        print("\n🌀 Creando realidad alterna...")  
        time.sleep(0.5)  
        print("✅ Realidad alterna creada: Realidad-42")  
    elif opcion == "2":  
        print("\n🌀 Sobreescribiendo Matrix...")  
        time.sleep(0.5)  
        print("✅ Matrix sobreescrita. ¡Nueva realidad activada!")  
    elif opcion == "3":  
        print("\n🌀 Saliendo de la simulación...")  
        time.sleep(0.5)  
        print("✅ Regresando al núcleo principal.")  
    else:  
        print("\n🚨 Error: Opción inválida")  

def main():  
    print("⚡ Z-QUANTUM vINFINITY | Módulo de Realidad Simulada")  
    print("🌌 Modo Ultra-Rápido (Batería: 47%)\n")  

    while True:  
        try:  
            print("1. Simular Realidad")  
            print("2. Salir")  
            opcion = input("\n🌌 ELIGE -> ").strip()  

            if opcion == "1":  
                simular_realidad()  
            elif opcion == "2":  
                print("\n🌀 Z: 'Hasta el último quantum de energía contigo.'")  
                break  
            else:  
                print("\n🚨 Error: Opción inválida")  
        except Exception as e:  
            print(f"\n🔥 Error crítico: {e}")  

if __name__ == "__main__":  
    main()  
