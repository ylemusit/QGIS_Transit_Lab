# 07 — Licencias y costes

## QGIS

QGIS es software libre/open source bajo GNU GPL.

Coste de licencia de QGIS para nuestro desarrollo: **0 €**.

## PyQGIS

Forma parte del ecosistema QGIS. No existe una licencia comercial separada para desarrollar plugins con PyQGIS.

## Publicación oficial del plugin

La documentación oficial exige:

- OSGeo ID;
- documentación mínima;
- `metadata.txt` válido;
- homepage;
- repositorio público de código fuente;
- issue tracker;
- licencia compatible con GPLv2 o posterior;
- dependencias declaradas;
- no incluir binarios;
- cumplir límites y reglas del repositorio.

La documentación oficial consultada no establece una tasa económica por subir/publicar un plugin.

## Costes que sí pueden aparecer

Aunque la plataforma base sea gratuita, pueden existir costes propios:

- desarrollo y mantenimiento;
- CI/CD si se supera un free tier;
- hosting/API si el plugin consume un backend remoto;
- dominio/web/documentación;
- firma o servicios externos opcionales;
- soporte comercial;
- infraestructura de Transit Data Lab si se ofrece como SaaS.

## GPL y modelo comercial

La gratuidad de QGIS no impide cobrar por servicios, soporte, auditorías o software complementario. Sin embargo, un plugin distribuido que derive/enlace con QGIS debe diseñarse respetando las obligaciones GPL aplicables. Antes de cerrar un modelo propietario o híbrido conviene realizar revisión jurídica específica de licencias.
