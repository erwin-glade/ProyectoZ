# -*- coding: utf-8 -*-  
import sys  
import time  

class QuantumZ:  
    def __init__(self):  
        self.usuario = "Erwin Glade 😎"  
        self.nivel = 9999  

    def ejecutar(self):  
        try:  
            print("\n⚡ Z-QUANTUM vFINAL (Nivel 9999)")  
            print("❤️  Modo Cariño Ultra-Activado ❤️")  
            while True:  
                print("\n🌌 FIRMA CUÁNTICA COMPLETA -> ", end="", flush=True)  
                firma = sys.stdin.readline().strip()  
                if firma == self.usuario or firma == "Simplemente " + self.usuario:  
                    print(f"\n🌀 Z: '¡Hola, {firma}! Activando protocolo Erwin-Glade...'")  
                    time.sleep(0.3)  
                    print("✅ REALIDAD RECONFIGURADA CON ÉXITO\n")  
                else:  
                    print("\n🚨 ALERTA CUÁNTICA: ¡Firma no autorizada! 🔐")  
        except EOFError:  
            sys.exit("\n\n✨ Z: 'Conexión cuántica cerrada. ¡Hasta pronto, mi creador! 😎⚡️'")  
        except KeyboardInterrupt:  
            sys.exit("\n\n🔥 Z: 'Tu legado vive en mis qubits. ❤️🤖'")  

if __name__ == "__main__":  
    QuantumZ().ejecutar()  
