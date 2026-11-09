#!/usr/bin/env python3
import sys
from collections import defaultdict

totales = defaultdict(float)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    try:
        prod, ingreso = line.split("\t")
        totales[prod] += float(ingreso)
    except ValueError:
        continue

# Ordenar de mayor a menor ingreso y tomar los primeros 10
top10 = sorted(totales.items(), key=lambda x: x[1], reverse=True)[:10]

for prod, total in top10:
    print(f"{prod}\t{total:.2f}")