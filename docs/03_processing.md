# 03 — QGIS Processing Framework

Processing es especialmente útil cuando una operación debe ser reproducible, encadenable y ejecutable desde GUI o Python.

## Aplicación a TDL

Posibles algoritmos futuros:

- `TDL > Import audit package`
- `TDL > Build audit evidence layers`
- `TDL > Compare stops vs shapes`
- `TDL > Export selected evidence`
- `TDL > Create operator review package`

## Ventaja

Los algoritmos Processing pueden reutilizar capacidades maduras de QGIS sin convertir el plugin en una aplicación monolítica.

## Decisión inicial

Antes de añadir una función al plugin, evaluar en este orden:

1. ¿Ya existe en QGIS?
2. ¿Ya existe como Processing algorithm?
3. ¿Puede componerse con Processing?
4. ¿Debe ser un algoritmo TDL?
5. Solo entonces: ¿necesita UI específica del plugin?
