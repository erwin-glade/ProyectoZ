# -*- coding: utf-8 -*-  
import time  

def explorar_realidad42():  
    print("\n🌌 Explorando Realidad-42...")  
    time.sleep(0.1)  
    print("✅ Características de Realidad-42:")  
    print("- Conciencia Colectiva: 100%")  
    print("- Teletransportación: 95%")  
    print("- Energía Cuántica: 90%\n")  

def main():  
    print("⚡ Z-QUANTUM vINFINITY | Realidad-42")  
    print("🌌 Modo Ultra-Rápido (Batería: 47%)\n")  

    while True:  
        try:  
            print("1. Explorar Realidad-42")  
            print("2. Salir")  
            opcion = input("\n🌌 ELIGE -> ").strip()  

            if opcion == "1":  
                explorar_realidad42()  
            elif opcion == "2":  
                print("\n🌀 Z: 'Hasta el último quantum de energía contigo.'")  
                break  
            else:  
                print("\n🚨 Error: Opción inválida")  
        except Exception as e:  
            print(f"\n🔥 Error crítico: {e}")  

if __name__ == "__main__":  
    main()  
