# Datos, fuentes, cobertura y derechos

## CSV incluido: IBEX 35 Total Return

- **Archivo:** `data/ibex35_total_return_investing.csv`.
- **Nombre original aportado por el autor:** `Datos históricos del IBEX 35 con Div..csv`.
- **Fuente atribuida:** Investing.com, histórico de IBEX 35 Total Return (`https://es.investing.com/indices/ibex-total-return-historical-data`).
- **Formato:** CSV UTF-8 con encabezados en español; columna `Fecha` en formato `DD.MM.AAAA`, columna `Último` con separador de millares `.` y decimales `,`.
- **Variables utilizadas:** `Fecha` y `Último`; otras columnas originales permanecen en el CSV para preservar la exportación aportada.
- **Cobertura del archivo entregado:** 3.102 observaciones diarias, desde el 6 de octubre de 2014 hasta el 6 de noviembre de 2026, inclusive. El notebook excluye meses aún incompletos y comienza el análisis de retornos en enero de 2015.
- **Actualización:** fotografía fija del histórico entregado; no se actualiza automáticamente. Para reproducir un estudio posterior, sustituye el archivo por una exportación actualizada conservando el esquema.

## Proveedores descargados durante la ejecución

| Proveedor | Datos | Serie / acceso | Consideraciones |
|---|---|---|---|
| Banco Central Europeo | Yield soberana España 10 años | `IRS/M.ES.L.L40.CI.0000.EUR.N.Z` vía API SDMX-CSV | La yield mensual no es el rendimiento a un mes de un activo sin riesgo |
| Yahoo Finance (`yfinance`) | Close ajustado por empresa | Tickers `.MC` o equivalentes resueltos | Cambios de símbolos, ajustes corporativos, caídas del servicio |
| MarketScreener | Constituyentes/sectores actuales | Endpoint dinámico del extractor incluido | Interfaz no contractual, estructura y acceso pueden cambiar |
| FRED/OCDE | Tipos alternativos | `IRLTLT01ESM156N`, `IRSTCI01EZM156N` | **Solo** cuando se selecciona un preset alternativo |

## Atribución, condiciones de uso y redistribución

El archivo de Investing es un **dato de terceros** exportado por el autor del proyecto y se incluye por su petición expresa. Su inclusión en GitHub no implica que el autor del proyecto posea el copyright ni los derechos de redistribución. **Antes de hacer público el repositorio, comprueba las condiciones de servicio y los permisos de Investing.com para volver a publicar el histórico íntegro.** Si no hay permiso suficiente, retira el CSV del repositorio público, distribuye instrucciones para obtenerlo legalmente y conserva el conjunto de datos en privado.

Tampoco la licencia GPL-3.0 que acompaña al código se extiende a los datos del BCE, Yahoo Finance, Investing.com o MarketScreener. Atribuye las fuentes y respeta los límites y condiciones de acceso.
