# -*- coding: utf-8 -*-  
import os  
import time  

def ejecutar_comando(comando):  
    print(f"\n💻 Ejecutando: {comando}")  
    time.sleep(0.1)  
    os.system(comando)  
    print("✅ Comando ejecutado en 0.1 segundos.\n")  

def main():  
    print("⚡ Z-QUANTUM vINFINITY | Comandos iSH Shell")  
    print("🌌 Modo Ultra-Rápido (Batería: 3% = ∞)\n")  

    while True:  
        try:  
            print("1. Listar archivos y directorios (ls -la)")  
            print("2. Verificar espacio en disco (df -h)")  
            print("3. Verificar memoria libre (free -m)")  
            print("4. Verificar versión de Python (python3 --version)")  
            print("5. Verificar IP (ifconfig)")  
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
                ejecutar_comando("ifconfig")  
            elif opcion == "6":  
                print("\n🌀 Z: 'Hasta el último quantum de energía contigo.'")  
                break  
            else:  
                print("\n🚨 Error: Opción inválida")  
        except Exception as e:  
            print(f"\n🔥 Error crítico: {e}")  

if __name__ == "__main__":  
    main()  
