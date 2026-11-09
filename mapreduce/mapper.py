#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    # Ignorar líneas vacías y el encabezado del CSV
    if not line or line.startswith("id,"):
        continue
    
    parts = line.split(",")
    if len(parts) != 8:
        continue
        
    try:
        producto = parts[4]
        cantidad = float(parts[5])
        precio = float(parts[6])
        ingreso = cantidad * precio
        
        # Emite: NOMBRE_PRODUCTO \t INGRESO
        print(f"{producto}\t{ingreso}")
    except ValueError:
        # Ignora líneas mal formadas sin cortar el job
        continue