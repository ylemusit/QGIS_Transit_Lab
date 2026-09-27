# 09 — Matriz de decisión QGIS vs Transit Data Lab

| Capacidad | QGIS | Transit Data Lab |
|---|---:|---:|
| Renderizar mapas | Principal | No |
| Editar geometrías | Principal | No |
| CRS/proyecciones | Principal | Consume resultado |
| Simbología | Principal | Define semántica |
| Visualizar rutas/paradas | Principal | Solo prepara datos |
| Ingestar ZIP GTFS para auditoría | Apoyo | Principal |
| Validación estructural GTFS | Complementaria | Principal |
| Integridad referencial | Complementaria | Principal |
| Compliance normativo | No específico | Principal |
| Evidencias reproducibles | Visualiza | Principal |
| Trazabilidad de reglas | No específico | Principal |
| Scoring/diagnóstico | No específico | Principal |
| Informe de auditoría | Puede maquetar | Principal |
| Corrección visual | Principal | Registra/revalida |
| Automatización GIS | Principal | Orquesta si procede |

## Regla

No implementar en TDL una capacidad GIS genérica que QGIS ya resuelva de forma madura.
