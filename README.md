# QGIS + Transit Data Lab Research

Repositorio técnico para estudiar QGIS al nivel necesario para integrar Transit Data Lab con su ecosistema sin reconstruir capacidades GIS ya maduras.

## Objetivos

1. Conocer QGIS y PyQGIS con profundidad suficiente para tomar decisiones de arquitectura.
2. Catalogar qué capacidades GIS y GTFS ya existen.
3. Definir la frontera funcional entre QGIS y Transit Data Lab.
4. Diseñar y prototipar un plugin `Transit Data Lab for QGIS`.
5. Documentar licencias, publicación, dependencias, testing y costes.

## Baseline técnica (27-09-2026)

- QGIS Latest: **4.2.2 “Belém do Pará”** (28-08-2026).
- QGIS LTR: **3.44.14 “Solothurn”**.
- QGIS 4.x usa Qt6.
- QGIS es software libre/open source bajo GPL.
- Los plugins Python se desarrollan con PyQGIS.
- Para publicar en el repositorio oficial, el plugin debe cumplir las reglas de metadata, documentación, licencia y repositorio público.

## Estructura

- `docs/00_scope.md`: alcance del estudio.
- `docs/01_qgis_architecture.md`: arquitectura conceptual de QGIS.
- `docs/02_pyqgis.md`: API Python y puntos de integración.
- `docs/03_processing.md`: Processing Framework y automatización.
- `docs/04_plugin_system.md`: arquitectura de plugins.
- `docs/05_gtfs_ecosystem.md`: capacidades GTFS ya existentes.
- `docs/06_tdl_plugin_design.md`: diseño propuesto del plugin de Transit Data Lab.
- `docs/07_licensing_costs.md`: licencias, costes y restricciones.
- `docs/08_development_roadmap.md`: roadmap de investigación y desarrollo.
- `docs/09_decision_matrix.md`: qué hace QGIS vs qué hace Transit Data Lab.
- `references/SOURCES.md`: fuentes oficiales.
- `plugin/transit_data_lab_qgis/`: esqueleto mínimo inicial de plugin.

## Principio arquitectónico

> QGIS debe resolver GIS, edición y visualización. Transit Data Lab debe resolver ingestión, validación, compliance, evidencias, auditoría y lógica específica de transporte.

Este repositorio no pretende competir con QGIS. Pretende convertirlo en una plataforma de visualización e inspección para los resultados generados por Transit Data Lab.
