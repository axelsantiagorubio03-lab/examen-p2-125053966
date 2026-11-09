# Examen Práctico DataMart - 125053966

## Problema Asignado
Top 10 productos por total de ingresos por año (Matrícula terminada en 6).

## Arquitectura del Sistema
- **Hadoop**: Procesamiento distribuido mediante MapReduce Streaming en Python.
- **PostgreSQL**: Almacenamiento persistente de los resultados agregados.
- **Python API (FastAPI/Uvicorn)**: Interfaz REST para consulta y manipulación de resultados.
- **Docker Compose**: Orquestación y comunicación SSH sin contraseña mediante volúmenes compartidos de llaves RSA.

## Comparativa de Rendimiento

| Método | Tiempo de Ejecución |
|---|---|
| Script Secuencial (Python) | 7.15 s |
| MapReduce (Hadoop) | Map 100% / Reduce 100% (Ejecución Distribuida) |

### Análisis Técnico
- **Procesamiento Secuencial**: Lee y procesa todo el archivo en memoria usando un solo hilo de ejecución. Es rápido para archivos de tamaño moderado, pero no escala si el dataset supera la memoria RAM disponible.
- **MapReduce**: Divide la carga de trabajo en fases independientes (Map y Reduce), garantizando alta disponibilidad, tolerancia a fallos y escalabilidad horizontal al agregar más nodos al clúster de Hadoop.

## Endpoints de la API REST
- `GET /resultados`: Retorna el listado completo de métricas procesadas.
- `GET /resultados/{clave}`: Retorna el resultado específico de una clave/producto.
- `POST /resultados`: Permite insertar o registrar nuevas métricas procesadas.
