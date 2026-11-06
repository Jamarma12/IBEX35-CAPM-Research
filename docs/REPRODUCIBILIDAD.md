# Reproducción y validación

## Preparación

1. Instala Python 3.10 o posterior.
2. Clona el repositorio o descomprime el paquete completo.
3. Crea un entorno virtual y ejecuta `python -m pip install -r requirements.txt`.
4. Lanza `jupyter lab` desde la raíz; abre `notebooks/CAPM_IBEX35_CSV_TR_BCE.ipynb`.
5. Comprueba que existe `data/ibex35_total_return_investing.csv`.
6. Ejecuta las celdas en orden. La extracción de MarketScreener está integrada en el notebook y puede fallar si la API cambia o bloquea la petición.

Para Colab, sube el notebook y el CSV a `/content/Datos históricos del IBEX 35 con Div..csv`, o monta Drive y ajusta `CSV_CANDIDATES` a su ruta. Instala los paquetes de `requirements.txt` en una celda separada.

## Validación local, sin red

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

Estos comandos verifican sintaxis Python de las celdas, datos CSV, cronología y presencia de componentes clave. No ejecutan la descarga de acciones, la API del BCE ni el scraper.

## Qué esperar en el notebook

- Archivo CSV parseable con 3.102 días y 145 cierres mensuales entre octubre 2014 y octubre 2026 (incluidos), antes de aplicar el inicio de rentabilidades.
- El número de meses realmente estimados depende de la disponibilidad de Yahoo y del BCE.
- El universo actual de MarketScreener cambia con rebalanceos, retiradas y nuevas incorporaciones; no se garantiza exactamente 35 valores estimables.
- Las salidas se generan en `resultados_capm_demo/`, excluidas del control de versiones.

## Registro de integridad

`sha256sum data/ibex35_total_return_investing.csv` (Linux/macOS) o `Get-FileHash data/ibex35_total_return_investing.csv -Algorithm SHA256` (PowerShell). El checksum de la exportación original se encuentra en `docs/CAMBIOS.md`.

## Publicación

Antes de marcar una versión como estable: comprueba que todos los proveedores respondan, la cobertura temporal, los nombres y tickers resueltos, el Excel exportado, el orden de ejecución del notebook y el cumplimiento de licencias de los datos. Los tests CI son **offline** y no acreditan una ejecución con datos de mercado en directo.
