# 06 — Diseño propuesto: Transit Data Lab for QGIS

## Propósito

El plugin NO será un reemplazo de GTFS Explorer. Será una interfaz de inspección para auditorías producidas por Transit Data Lab.

## MVP

### Acción 1 — Abrir auditoría TDL

Seleccionar un paquete de resultados generado por TDL.

### Acción 2 — Crear capas de evidencia

Ejemplos:

- `TDL - Critical`
- `TDL - High`
- `TDL - Medium`
- `TDL - Stops`
- `TDL - Shapes`
- `TDL - Referential integrity`

### Acción 3 — Panel de evidencia

Al seleccionar un error:

- Rule ID
- Severidad
- Archivo origen
- Entidad afectada
- Valor observado
- Valor esperado
- Explicación
- Recomendación

### Acción 4 — Zoom a evidencia

Centrar/seleccionar el objeto afectado.

### Acción 5 — Marcar estado de revisión

Estados locales posibles:

- pendiente;
- revisado;
- falso positivo;
- corregido;
- requiere operador.

## Contrato ideal entre TDL y QGIS

TDL debería exportar un `audit-package` estable, por ejemplo:

```text
operator_audit/
├── manifest.json
├── summary.json
├── evidence.gpkg
├── findings.csv
├── report.pdf
└── source_hashes.json
```

El plugin se limita a interpretar ese contrato y representarlo.

## Arquitectura

```text
GTFS / NeTEx / SIRI
       ↓
Transit Data Lab Core
       ↓
Validation + Compliance + Evidence
       ↓
Audit Package
       ↓
QGIS Plugin
       ↓
Visual inspection / correction workflow
```
