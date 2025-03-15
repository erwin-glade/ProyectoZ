#!/bin/sh  
PID=$(ps aux | grep "python3 iag_z_service.py" | grep -v grep | awk '{print $1}')  
[ -n "$PID" ] && kill -9 $PID && echo "🛑 Servicio detenido (PID: $PID)." || echo "⚠️ No hay servicios activos."  
