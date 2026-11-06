# Trazabilidad de la preparación para GitHub

## Versión original recibida

- Notebook: `CAPM_IBEX35_CSV_TR_BCE.ipynb`, con 13 celdas (8 de código y 5 de Markdown, una vacía).
- CSV: `Datos históricos del IBEX 35 con Div..csv`, exportación de Investing.com.

## Cambios deliberadamente limitados

1. **Introducción reescrita**: elimina referencias erróneas a FRED como fuente principal y la advertencia obsoleta que sugería que el benchmark era `^IBEX`. Documenta Investing CSV + Yahoo + BCE + MarketScreener, incluyendo límites del uso del rendimiento soberano a 10 años.
2. **Rutas portables**: `CSV_INVESTING` se resuelve desde `data/` en la raíz o desde `notebooks/`, con alternativa específica para Colab. El fichero del autor se conserva **sin alterar su contenido**, renombrado en `data/`.
3. **Instalación**: se sustituye el `!pip install` ejecutado automáticamente por instrucciones para instalar `requirements.txt` fuera del notebook. Esto permite usar Jupyter local y evita descargas forzadas en cada ejecución.
4. **Metodología**: la sección 05 distingue la sensibilidad `Ke_rf_actual` del CAPM histórico; el texto de rolling describe su alcance real.
5. **Limpieza de publicación**: se eliminan salidas y contadores de ejecuciones anteriores, se elimina una celda Markdown vacía; **se conservan las ocho celdas de código**, las funciones, figuras, scraper y exportaciones. No se eliminan los análisis.
6. **Documentación y QA**: README, metodología, fuentes, reproducción, licencia GPL-3.0 (coherente con la ya publicada en GitHub), cita, `.gitignore`, dependencias, CI y pruebas offline.

## No validado

No se ha completado una nueva ejecución integral contra Yahoo Finance, BCE y MarketScreener. Los resultados de una ejecución posterior pueden diferir por actualizaciones de datos y composición del universo.

**SHA256 del CSV proporcionado:** `3d1ce017ed88a1ddde5093d47d2b15a631b064ddf5c9b4a3563dc0fdb5dc908d`.

**Prueba sintética adicional:** ejecutadas las celdas de preparación, estimaciones CAPM, panel SCL, SML y rolling utilizando series de acciones sintéticas y una respuesta BCE simulada. Se produjeron seis regresiones y 636 predicciones rolling. Esta prueba verifica el flujo sin acceso a red, **no** la calidad de los datos ni el scraper de MarketScreener.
