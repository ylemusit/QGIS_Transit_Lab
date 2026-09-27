# 01 — Arquitectura conceptual de QGIS

QGIS es una plataforma GIS extensible. Para Transit Data Lab interesa separar cinco capas:

1. **Core GIS** — capas vectoriales/raster, geometrías, CRS, proveedores de datos.
2. **Desktop UI** — mapa, panel de capas, tablas de atributos, edición y simbología.
3. **Processing Framework** — ejecución reproducible de algoritmos y modelos.
4. **PyQGIS** — API Python prácticamente equivalente a gran parte de la API C++.
5. **Plugin system** — extensión de menús, toolbars, docks, procesamiento y flujos específicos.

## Componentes de interés

- `QgsProject`: proyecto activo.
- `QgsVectorLayer`: capas vectoriales.
- `QgsFeature`: entidades y atributos.
- `QgsGeometry`: geometría.
- `QgsCoordinateReferenceSystem`: CRS.
- `QgsTask`: trabajos en background dentro de QGIS.
- `QgsProcessingAlgorithm`: algoritmos Processing.
- `QgisInterface / iface`: acceso a UI, canvas, menús y toolbars.

## Lectura para Transit Data Lab

El plugin no debería ser el motor de validación principal. Lo recomendable es que consuma resultados del motor TDL y los transforme en capas, estilos y acciones de inspección.
