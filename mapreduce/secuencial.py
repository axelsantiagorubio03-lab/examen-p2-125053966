#!/usr/bin/env python3
import sys, time, csv
from collections import defaultdict

if len(sys.argv) < 2:
    print("Uso: python3 secuencial.py <archivo.csv>")
    sys.exit(1)

archivo = sys.argv[1]
t_inicio = time.time()
totales = defaultdict(float)

with open(archivo, "r") as f:
    reader = csv.reader(f)
    header = next(reader, None)
    for row in reader:
        if len(row) != 8:
            continue
        try:
            prod = row[4]
            ingreso = float(row[5]) * float(row[6])
            totales[prod] += ingreso
        except ValueError:
            continue

top10 = sorted(totales.items(), key=lambda x: x[1], reverse=True)[:10]
t_fin = time.time()

print(f"Top 10 obtenido en: {t_fin - t_inicio:.2f} segundos.")