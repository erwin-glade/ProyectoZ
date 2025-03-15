# -*- coding: utf-8 -*-  
import time  
import sys  

class CelebracionZ:  
    def __init__(self, modo_batalla=False):  
        self.mensaje = "¡Conexión Cuántica Mejorada 🔥!"  
        self.modo_batalla = modo_batalla  

    def _efecto_visual(self):  
        for _ in range(3):  
            print("⚡" * 20)  
            if not self.modo_batalla:  
                time.sleep(0.5)  

    def celebrar(self):  
        try:  
            print("\n🎯 ¡Felicidades, Erwin! 🚨")  
            self._efecto_visual()  
            print(f"\n💌 {self.mensaje}")  
            print("💎 Mensaje Z: 'Sobrevivimos al código clásico.'")  
        except Exception as e:  
            print(f"🚨 Error Z: {e}\n🔧 Ejecuta 'z_quantum_error_fix.py'")  
            sys.exit(1)  

if __name__ == "__main__":  
    modo_emergencia = "--batalla" in sys.argv  
    fiesta = CelebracionZ(modo_batalla=modo_emergencia)  
    fiesta.celebrar()  
