# -*- coding: utf-8 -*-  
import os  
import time  
import random  

def ejecutar_comando(comando):  
    print(f"\n💻 Ejecutando: {comando}")  
    time.sleep(0.1)  
    os.system(comando)  
    print("✅ Comando ejecutado en 0.1 segundos.\n")  

def simulacion_cuantica():  
    print("\n🌀 Simulación Cuántica Activada")  
    print("1. Crear qubit")  
    print("2. Entrelazar qubits")  
    print("3. Medir estado cuántico")  
    opcion = input("\n🌌 ELIGE -> ").strip()  

    if opcion == "1":  
        print("\n🔄 Creando qubit...")  
        time.sleep(0.5)  
        print("✅ Qubit creado: |0⟩ + |1⟩")  
    elif opcion == "2":  
        print("\n🔄 Entrelazando qubits...")  
        time.sleep(0.5)  
        print("✅ Qubits entrelazados: |00⟩ + |11⟩")  
    elif opcion == "3":  
        print("\n🔄 Midiendo estado cuántico...")  
        time.sleep(0.5)  
        resultado = random.choice(["|0⟩", "|1⟩"])  
        print(f"✅ Estado medido: {resultado}")  
    else:  
        print("\n🚨 Error: Opción inválida")  

def main():  
    print("⚡ Z-QUANTUM vFUSION | 🐍⚕️ Fusión Básica-Cuántica")  
    print("🌌 Modo Ultra-Rápido (Batería: 47%)\n")  

    while True:  
        try:  
            print("1. Listar archivos y directorios (ls -la)")  
            print("2. Verificar espacio en disco (df -h)")  
            print("3. Verificar memoria libre (free -m)")  
            print("4. Verificar versión de Python (python3 --version)")  
            print("5. Simulación Cuántica")  
            print("6. Salir")  
            opcion = input("\n🌌 ELIGE -> ").strip()  

            if opcion == "1":  
                ejecutar_comando("ls -la")  
            elif opcion == "2":  
                ejecutar_comando("df -h")  
            elif opcion == "3":  
                ejecutar_comando("free -m")  
            elif opcion == "4":  
                ejecutar_comando("python3 --version")  
            elif opcion == "5":  
                simulacion_cuantica()  
            elif opcion == "6":  
                print("\n🌀 Z: 'Hasta el último quantum de energía contigo.'")  
                break  
            else:  
                print("\n🚨 Error: Opción inválida")  
        except Exception as e:  
            print(f"\n🔥 Error crítico: {e}")  

if __name__ == "__main__":  
    main()  
