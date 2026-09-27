# 04 — Sistema de plugins QGIS

## Plugin Python mínimo

Archivos esenciales:

- `metadata.txt`
- `__init__.py`
- módulo principal con la clase del plugin

`__init__.py` expone `classFactory(iface)`.

## Ciclo de vida típico

1. QGIS descubre el plugin.
2. Lee `metadata.txt`.
3. Ejecuta `classFactory(iface)`.
4. Instancia la clase del plugin.
5. `initGui()` registra acciones, menús o docks.
6. `unload()` limpia recursos.

## UI

Un plugin puede añadir:

- acciones de menú;
- botones de toolbar;
- dock widgets;
- diálogos;
- Processing providers;
- capas y estilos;
- interacción con el canvas.

## Compatibilidad

QGIS 4.x utiliza Qt6. El proyecto debe evitar dependencias antiguas de Qt5 y controlar explícitamente la matriz QGIS 3.44 LTR / 4.2+.
