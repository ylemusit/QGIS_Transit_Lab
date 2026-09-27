# 02 — PyQGIS

PyQGIS permite controlar QGIS desde Python.

## Formas oficiales de usar Python en QGIS

- Consola Python integrada.
- Plugins Python.
- Código al iniciar QGIS.
- Processing algorithms.
- Funciones de expresiones.
- Aplicaciones personalizadas basadas en la API.
- QGIS Server y plugins de servidor.

## Casos TDL

### Importación de resultados

Un resultado de auditoría puede materializarse como GeoPackage, GeoJSON o tablas y cargarse con `QgsVectorLayer`.

### Simbología automática

Errores `CRITICAL/HIGH/MEDIUM/LOW` pueden representarse por categorías sin recrear un renderer GIS propio.

### Navegación a evidencia

El plugin puede seleccionar una evidencia y centrar el canvas en la geometría afectada.

### Atributos de auditoría sugeridos

- `audit_id`
- `rule_id`
- `severity`
- `entity_type`
- `entity_id`
- `message`
- `expected`
- `observed`
- `source_file`
- `evidence_ref`

## Norma de arquitectura

PyQGIS será adaptador/presentación. Las reglas regulatorias y GTFS seguirán siendo agnósticas de QGIS.
